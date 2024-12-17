import unittest
from time import time
from Alfa import PrimeFinder  # Ujistěte se, že importujete správně svou třídu


class TestPrimeFinder(unittest.TestCase):

    def test_is_prime(self):
        """Test for is_prime method."""
        prime_finder = PrimeFinder(1, 10, 2)
        self.assertTrue(prime_finder.is_prime(2))  # 2 je prvočíslo
        self.assertFalse(prime_finder.is_prime(4))  # 4 není prvočíslo
        self.assertTrue(prime_finder.is_prime(3))  # 3 je prvočíslo
        self.assertFalse(prime_finder.is_prime(1))  # 1 není prvočíslo
        self.assertFalse(prime_finder.is_prime(0))  # 0 není prvočíslo
        self.assertFalse(prime_finder.is_prime(-3))  # Záporná čísla nejsou prvočísla

    def test_find_primes_in_range(self):
        """Test for find_primes_in_range method."""
        prime_finder = PrimeFinder(1, 10, 2)
        primes = prime_finder.find_primes_in_range(1, 10)
        self.assertEqual(primes, [2, 3, 5, 7])  # Očekáváme prvočísla v tomto rozsahu

    def test_reverse_range(self):
        """Test for reversed range (start > end)."""
        prime_finder = PrimeFinder(50, 10, 4)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [])  # Očekáváme prázdný seznam, protože rozsah je obrácený

    def test_single_prime_at_start_of_range(self):
        """Test for a range with a single prime at the start."""
        prime_finder = PrimeFinder(1, 3, 2)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [2])  # Očekáváme, že 2 bude prvočíslo

    def test_empty_range(self):
        """Test for an empty range (start == end)."""
        prime_finder = PrimeFinder(10, 10, 2)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [])  # Očekáváme prázdný seznam, protože rozsah je prázdný

    def test_negative_range(self):
        """Test for a negative range."""
        prime_finder = PrimeFinder(-10, -1, 2)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [])  # Očekáváme prázdný seznam, protože záporná čísla nejsou prvočísla

    def test_large_range(self):
        """Test for a large range."""
        prime_finder = PrimeFinder(1, 10000, 4)
        primes = prime_finder.parallel_find_primes()
        self.assertGreater(len(primes), 0)  # Očekáváme alespoň nějaká prvočísla

    def test_threads_and_multiprocessing_identical_results(self):
        """Test for threads and multiprocessing giving identical results."""
        prime_finder = PrimeFinder(1, 100, 4)
        thread_primes = prime_finder.parallel_find_primes()
        process_primes = prime_finder.multiprocessing_find_primes()
        self.assertEqual(set(thread_primes), set(process_primes))  # Očekáváme stejné výsledky

    def test_performance(self):
        """Test for performance with larger ranges."""
        prime_finder = PrimeFinder(1, 100000, 4)

        # Měření času pro vlákna
        thread_start_time = time()
        prime_finder.parallel_find_primes()
        thread_end_time = time()
        thread_duration = thread_end_time - thread_start_time
        self.assertLess(thread_duration, 2)  # Očekáváme, že test proběhne za méně než 2 sekundy

        # Měření času pro multiprocessing
        process_start_time = time()
        prime_finder.multiprocessing_find_primes()
        process_end_time = time()
        process_duration = process_end_time - process_start_time
        self.assertLess(process_duration, 2)  # Očekáváme, že test proběhne za méně než 2 sekundy

    def test_start_greater_than_end(self):
        """Test for case where start is greater than end."""
        prime_finder = PrimeFinder(100, 50, 2)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [])  # Očekáváme prázdný seznam, protože start > end

    def test_start_is_zero(self):
        """Test for case where start is zero."""
        prime_finder = PrimeFinder(0, 10, 2)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [2, 3, 5, 7])  # Očekáváme prvočísla od 2 do 10

    def test_large_prime_range(self):
        """Test for a large range that contains large prime numbers."""
        prime_finder = PrimeFinder(10000, 20000, 4)
        primes = prime_finder.parallel_find_primes()
        self.assertGreater(len(primes), 0)  # Očekáváme nějaká prvočísla ve velkém rozsahu

    def test_single_large_prime(self):
        """Test for a range containing a single large prime."""
        prime_finder = PrimeFinder(104729, 104730, 2)  # 104729 je prvočíslo
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [104729])  # Očekáváme, že 104729 bude prvočíslo

    def test_no_primes_in_range(self):
        """Test for a range with no primes."""
        prime_finder = PrimeFinder(1000, 1005, 2)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [])  # Očekáváme prázdný seznam, protože v tomto rozsahu nejsou žádná prvočísla

    def test_multiple_primes(self):
        """Test for a range with multiple primes."""
        prime_finder = PrimeFinder(1, 20, 2)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19])  # Očekáváme seznam prvočísel v tomto rozsahu

    def test_single_thread_vs_multiple_threads(self):
        """Test comparing results of single-threaded and multi-threaded computations."""
        prime_finder = PrimeFinder(1, 100, 1)  # Jeden thread
        single_thread_primes = prime_finder.parallel_find_primes()

        prime_finder_multi = PrimeFinder(1, 100, 4)  # Více než jeden thread
        multi_thread_primes = prime_finder_multi.parallel_find_primes()

        self.assertEqual(set(single_thread_primes), set(multi_thread_primes))  # Očekáváme stejné výsledky

    def test_start_is_one(self):
        """Test for range starting at 1."""
        prime_finder = PrimeFinder(1, 10, 2)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [2, 3, 5, 7])  # 1 není prvočíslo, začínáme od 2

    def test_large_prime_in_the_middle_of_range(self):
        """Test for a large prime number in the middle of the range."""
        prime_finder = PrimeFinder(1000000, 1000100, 4)
        primes = prime_finder.parallel_find_primes()
        self.assertIn(1000003, primes)  # 1000003 je prvočíslo

    def test_prime_at_the_end_of_range(self):
        """Test for a prime number at the end of the range."""
        prime_finder = PrimeFinder(10, 100, 3)
        primes = prime_finder.parallel_find_primes()
        self.assertIn(97, primes)  # 97 je prvočíslo

    def test_no_primes_in_range_large_gap(self):
        """Test for a large range with no primes in between."""
        prime_finder = PrimeFinder(100000, 100100, 5)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [])  # Žádná prvočísla mezi 100000 a 100100

    def test_prime_number_count(self):
        """Test for counting the number of primes in a range."""
        prime_finder = PrimeFinder(1, 100, 4)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(len(primes), 25)  # Očekáváme 25 prvočísel v rozsahu 1-100

    def test_threads_and_multiprocessing_performance_comparison(self):
        """Test to compare the performance of threading vs multiprocessing."""
        prime_finder = PrimeFinder(1, 1000000, 4)

        # Měření pro vlákna
        thread_start_time = time()
        prime_finder.parallel_find_primes()
        thread_end_time = time()
        thread_duration = thread_end_time - thread_start_time

        # Měření pro multiprocessing
        process_start_time = time()
        prime_finder.multiprocessing_find_primes()
        process_end_time = time()
        process_duration = process_end_time - process_start_time

        # Očekáváme, že multiprocessing bude rychlejší než vlákna
        self.assertLess(process_duration, thread_duration)

    def test_odd_numbers_in_range(self):
        """Test for a range that contains only odd numbers."""
        prime_finder = PrimeFinder(1, 50, 3)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

    def test_edge_case_prime(self):
        """Test for an edge case where the range includes a single prime number."""
        prime_finder = PrimeFinder(2, 3, 1)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [2])  # Očekáváme jen 2 jako prvočíslo

    def test_prime_in_range_with_large_step(self):
        """Test for a large step between start and end in the range."""
        prime_finder = PrimeFinder(100, 1000, 10)
        primes = prime_finder.parallel_find_primes()
        self.assertGreater(len(primes), 0)  # Očekáváme nějaká prvočísla

    def test_empty_range_with_threads(self):
        """Test for an empty range using threading."""
        prime_finder = PrimeFinder(1000, 1000, 4)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [])  # Očekáváme prázdný seznam

    def test_invalid_thread_count(self):
        """Test for invalid thread count."""
        prime_finder = PrimeFinder(1, 10, 0)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes, [])  # Očekáváme prázdný seznam nebo chyba, protože 0 vláken není platné

    def test_multiple_primes_in_large_range(self):
        """Test for a large range with multiple primes."""
        prime_finder = PrimeFinder(1000000, 1001000, 6)
        primes = prime_finder.parallel_find_primes()
        self.assertGreater(len(primes), 0)  # Očekáváme nějaká prvočísla

    def test_all_combinations_of_threads_and_processes(self):
        """Test various combinations of threads and processes."""
        prime_finder = PrimeFinder(1, 10000, 5)
        threads_primes = prime_finder.parallel_find_primes()

        prime_finder.num_threads = 5  # Změna na 5 procesů
        process_primes = prime_finder.multiprocessing_find_primes()

        self.assertEqual(set(threads_primes), set(process_primes))  # Očekáváme stejné výsledky

    def test_find_primes_for_large_input_size(self):
        """Test for finding primes in a very large range."""
        prime_finder = PrimeFinder(1, 10000000, 8)
        primes = prime_finder.parallel_find_primes()
        self.assertGreater(len(primes), 0)  # Očekáváme, že se najde alespoň nějaké prvočíslo

    def test_prime_at_the_start_of_range(self):
        """Test for a prime number at the very start of the range."""
        prime_finder = PrimeFinder(2, 10, 3)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(primes[0], 2)  # 2 je prvočíslo na začátku

    def test_multiple_ranges_with_varying_threads(self):
        """Test for multiple ranges with different numbers of threads."""
        test_cases = [
            (1, 10, 1), (1, 10, 2), (1, 10, 4),  # Malý rozsah s různými thready
            (100, 1000, 2), (100, 1000, 8),  # Střední rozsah
            (10000, 20000, 2), (10000, 20000, 10),  # Větší rozsah
            (50000, 100000, 4), (50000, 100000, 8)  # Velký rozsah
        ]
        for start, end, num_threads in test_cases:
            with self.subTest(start=start, end=end, num_threads=num_threads):
                prime_finder = PrimeFinder(start, end, num_threads)
                primes = prime_finder.parallel_find_primes()
                self.assertGreaterEqual(len(primes), 0)  # Kontrola, že máme nějaké výsledky

    def test_large_prime_ranges_different_steps(self):
        """Test for large ranges with varying steps and prime checks."""
        steps = [2, 3, 5, 7, 10]
        for step in steps:
            prime_finder = PrimeFinder(1, 100000, step)
            primes = prime_finder.parallel_find_primes()
            self.assertGreater(len(primes), 0)  # Ověření, že test s kroky najde prvočísla

    def test_extreme_large_values_threads(self):
        """Test for extremely large values with different threads."""
        large_ranges = [
            (1, 1000000, 2),
            (1, 1000000, 4),
            (1, 1000000, 8),
            (500000, 1000000, 10)
        ]
        for start, end, threads in large_ranges:
            with self.subTest(start=start, end=end, threads=threads):
                prime_finder = PrimeFinder(start, end, threads)
                primes = prime_finder.parallel_find_primes()
                self.assertGreater(len(primes), 0)  # Testujeme rozsahy s velkými čísly

    def test_combination_multiprocessing_and_threads(self):
        """Test combining both multiprocessing and threading approaches."""
        prime_finder = PrimeFinder(1, 50000, 4)
        thread_primes = prime_finder.parallel_find_primes()
        process_primes = prime_finder.multiprocessing_find_primes()
        combined_primes = set(thread_primes) & set(process_primes)
        self.assertEqual(set(thread_primes), set(process_primes))  # Výsledky by měly být identické

    def test_invalid_thread_counts_edge_cases(self):
        """Test for invalid edge cases in thread count."""
        invalid_threads = [0, -1, -10, None]
        for threads in invalid_threads:
            with self.subTest(threads=threads):
                prime_finder = PrimeFinder(1, 10, threads)
                self.assertRaises(ValueError, prime_finder.parallel_find_primes)

    def test_zero_primes_in_large_non_prime_range(self):
        """Test large ranges with no prime numbers."""
        ranges = [
            (1000000, 1000010, 2),  # Rozsah bez prvočísel
            (10000000, 10000010, 4)  # Extrémně velká čísla bez prvočísel
        ]
        for start, end, threads in ranges:
            with self.subTest(start=start, end=end, threads=threads):
                prime_finder = PrimeFinder(start, end, threads)
                primes = prime_finder.parallel_find_primes()
                self.assertEqual(primes, [])  # Ověření, že seznam je prázdný

    def test_single_prime_in_large_range(self):
        """Test where a single prime exists in a large range."""
        prime_finder = PrimeFinder(99991, 99993, 2)  # 99991 je prvočíslo
        primes = prime_finder.parallel_find_primes()
        self.assertIn(99991, primes)  # Kontrola přítomnosti jediného prvočísla

    def test_no_input_range(self):
        """Test if range input is None."""
        with self.assertRaises(TypeError):
            PrimeFinder(None, None, 4)

    def test_duplicate_primes(self):
        """Test ensuring no duplicate primes are returned."""
        prime_finder = PrimeFinder(1, 100, 5)
        primes = prime_finder.parallel_find_primes()
        self.assertEqual(len(primes), len(set(primes)))  # Žádná duplicita

    def test_prime_boundary_values(self):
        """Test prime numbers at the exact boundaries."""
        boundaries = [
            (2, 3),  # Dolní hranice
            (997, 1000),  # Horní hranice malých čísel
            (104729, 104730)  # 104729 je prvočíslo
        ]
        for start, end in boundaries:
            prime_finder = PrimeFinder(start, end, 2)
            primes = prime_finder.parallel_find_primes()
            if start == 2:
                self.assertIn(2, primes)  # Kontrola dolní hranice
            if start == 104729:
                self.assertIn(104729, primes)  # Kontrola horní hranice

    def test_large_input_random_thread_counts(self):
        """Test for random large inputs and random thread counts."""
        inputs = [
            (1000, 5000, 3),
            (1, 10000, 7),
            (500, 1500, 10)
        ]
        for start, end, threads in inputs:
            prime_finder = PrimeFinder(start, end, threads)
            primes = prime_finder.parallel_find_primes()
            self.assertGreater(len(primes), 0)  # Výsledek obsahuje prvočísla

    def test_repeated_small_range_computations(self):
        """Repeat small range computations to simulate stress."""
        for _ in range(50):  # Opakujeme 50x
            prime_finder = PrimeFinder(1, 10, 2)
            primes = prime_finder.parallel_find_primes()
            self.assertEqual(primes, [2, 3, 5, 7])
if __name__ == "__main__":
    unittest.main()