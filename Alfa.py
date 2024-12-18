import math
import threading
from multiprocessing import Pool
from time import time

class PrimeFinder:
    def __init__(self, start, end, num_threads):
        # Validace vstupů
        if not isinstance(start, int) or not isinstance(end, int) or not isinstance(num_threads, int):
            raise TypeError("All inputs must be integers.")
        if start < 0:
            raise ValueError("Start must be a non-negative integer.")
        if end < start:
            raise ValueError("End must be greater than or equal to start.")
        if num_threads <= 0:
            raise ValueError("Number of threads must be a positive integer.")

        self.start = start
        self.end = end
        self.num_threads = num_threads

    def is_prime(self, n):
        """Check if a number is a prime."""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def find_primes_in_range(self, start, end):
        """Find primes in a given range."""
        if start > end:  # Rozsah je prázdný
            return []
        if start < 2:  # Prvočísla začínají od 2
            start = 2
        return [n for n in range(start, end + 1) if self.is_prime(n)]

    def worker(self, start, end, result):
        """Worker function for threads."""
        primes = self.find_primes_in_range(start, end)
        result.extend(primes)

    def parallel_find_primes(self):
        """Find primes using threads."""
        step = math.ceil((self.end - self.start + 1) / self.num_threads)
        threads = []
        results = [[] for _ in range(self.num_threads)]

        for i in range(self.num_threads):
            thread_start = self.start + i * step
            thread_end = min(self.start + (i + 1) * step - 1, self.end)  # Abychom nepřesáhli rozsah
            thread = threading.Thread(target=self.worker, args=(thread_start, thread_end, results[i]))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Kombinace výsledků (odstranění duplicit a seřazení)
        primes = sorted(set(sum(results, [])))
        return primes

    def multiprocessing_find_primes(self):
        """Find primes using multiprocessing."""
        step = math.ceil((self.end - self.start + 1) / self.num_threads)
        ranges = [
            (self.start + i * step, min(self.start + (i + 1) * step - 1, self.end))
            for i in range(self.num_threads)
        ]

        with Pool(self.num_threads) as pool:
            results = pool.starmap(self.find_primes_in_range, ranges)

        # Kombinace výsledků (odstranění duplicit a seřazení)
        primes = sorted(set(sum(results, [])))
        return primes

    def save_to_file(self, primes, filename="primes.txt"):
        """Uloží seznam prvočísel do souboru."""
        try:
            with open(filename, "w") as f:
                f.write("\n".join(map(str, primes)))
            print(f"Primes successfully saved to {filename}")
        except Exception as e:
            print(f"Failed to save primes to file: {e}")

    def visualize_prime_distribution(self, primes):
        """Vizualizuje distribuci prvočísel."""
        try:
            import matplotlib.pyplot as plt

            # Spočítáme mezery mezi prvočísly
            gaps = [primes[i] - primes[i - 1] for i in range(1, len(primes))]
            plt.hist(gaps, bins=30, edgecolor="black", alpha=0.7)
            plt.title("Distribuce rozdílů mezi prvočísly")
            plt.xlabel("Rozdíl mezi sousedními prvočísly")
            plt.ylabel("Počet")
            plt.show()
        except ImportError:
            print("Matplotlib není nainstalován. Vizualizace se nepovedla.")
        except Exception as e:
            print(f"Chyba při vizualizaci: {e}")

if __name__ == "__main__":
    print("""
Welcome to the PrimeFinder program!

This is a demonstration program to showcase the use of threading and multiprocessing techniques 
for finding prime numbers within a specified range. 

In this program, you will:
- Input a range of numbers.
- Choose how many threads or processes to use for parallel computation.
- Use threading to divide the work into separate threads.
- Use multiprocessing to divide the work across multiple processes.
- Compare the performance of both methods.

This program is intended to help you understand the differences between threading and multiprocessing, 
and how they can be used to speed up computations in certain situations.

Let's get started by entering the range of numbers and the number of threads/processes to use.
""")

    start = None
    end = None
    num_threads = None

    while start is None:
        try:
            start = int(input("Enter the start of the range (>= 0): "))
            if start < 0:
                raise ValueError("Start of range must be non-negative.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
            start = None

    while end is None:
        try:
            end = int(input("Enter the end of the range (> start): "))
            if end <= start:
                raise ValueError("End of range must be greater than the start.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
            end = None

    while num_threads is None:
        try:
            num_threads = int(input("Enter the number of threads/processes to use (> 0): "))
            if num_threads <= 0:
                raise ValueError("Number of threads/processes must be positive.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
            num_threads = None

    prime_finder = PrimeFinder(start, end, num_threads)

    print(f"Finding primes in range {start} to {end} using {num_threads} threads and multiprocessing...")

    try:
        # Measure time for threads
        thread_start_time = time()
        thread_primes = prime_finder.parallel_find_primes()
        thread_end_time = time()
        print(f"Threads: Found {len(thread_primes)} primes in {thread_end_time - thread_start_time:.2f} seconds.")

        # Measure time for multiprocessing
        process_start_time = time()
        process_primes = prime_finder.multiprocessing_find_primes()
        process_end_time = time()
        print(f"Multiprocessing: Found {len(process_primes)} primes in {process_end_time - process_start_time:.2f} seconds.")

        # Ensure both methods found the same primes
        if set(thread_primes) != set(process_primes):
            print("Warning: Results differ between threads and multiprocessing!")
        else:
            print("Both methods produced the same results.")

        # Save results to file
        save_choice = input("Do you want to save the primes to a file? (yes/no): ").strip().lower()
        if save_choice in ("yes", "y"):
            prime_finder.save_to_file(thread_primes)

        # Visualize prime distribution
        visualize_choice = input("Do you want to visualize the prime distribution? (yes/no): ").strip().lower()
        if visualize_choice in ("yes", "y"):
            prime_finder.visualize_prime_distribution(thread_primes)

    except Exception as e:
        print(f"An error occurred during computation: {e}")
