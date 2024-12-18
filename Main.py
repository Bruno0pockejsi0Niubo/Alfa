
from Alfa import PrimeFinder  # Ujistěte se, že importujete správně svou třídu


import unittest

class TestPrimeFinder(unittest.TestCase):

    def setUp(self):
        """Nastavení základního prostředí pro testy."""
        self.prime_finder = PrimeFinder(0, 100, 4)

    def test_is_prime_basic(self):
        """Test základních prvočísel."""
        self.assertTrue(self.prime_finder.is_prime(2))
        self.assertTrue(self.prime_finder.is_prime(3))
        self.assertTrue(self.prime_finder.is_prime(5))
        self.assertTrue(self.prime_finder.is_prime(7))

    def test_is_prime_non_primes(self):
        """Test neprvočísel."""
        self.assertFalse(self.prime_finder.is_prime(1))
        self.assertFalse(self.prime_finder.is_prime(4))
        self.assertFalse(self.prime_finder.is_prime(6))
        self.assertFalse(self.prime_finder.is_prime(9))
        self.assertFalse(self.prime_finder.is_prime(15))

    def test_is_prime_edge_cases(self):
        """Test hraničních hodnot."""
        self.assertFalse(self.prime_finder.is_prime(0))
        self.assertFalse(self.prime_finder.is_prime(-1))
        self.assertFalse(self.prime_finder.is_prime(-10))
        self.assertTrue(self.prime_finder.is_prime(101))

    def test_find_primes_in_small_range(self):
        """Test vyhledání prvočísel v malém rozsahu."""
        self.assertEqual(
            self.prime_finder.find_primes_in_range(0, 10),
            [2, 3, 5, 7]
        )

    def test_find_primes_in_large_range(self):
        """Test vyhledání prvočísel ve větším rozsahu."""
        self.assertEqual(
            self.prime_finder.find_primes_in_range(10, 30),
            [11, 13, 17, 19, 23, 29]
        )

    def test_find_primes_no_primes(self):
        """Test rozsahu bez prvočísel."""
        self.assertEqual(
            self.prime_finder.find_primes_in_range(0, 1),
            []
        )

    def test_find_primes_reverse_range(self):
        """Test chybného vstupu, kde start > end."""
        self.assertEqual(
            self.prime_finder.find_primes_in_range(20, 10),
            []
        )

    def test_parallel_find_primes(self):
        """Test paralelního vyhledávání prvočísel."""
        prime_finder_parallel = PrimeFinder(0, 50, 4)
        primes = prime_finder_parallel.parallel_find_primes()
        self.assertEqual(
            primes,
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        )

    def test_multiprocessing_find_primes(self):
        """Test multiprocesního vyhledávání prvočísel."""
        prime_finder_multiprocess = PrimeFinder(0, 50, 4)
        primes = prime_finder_multiprocess.multiprocessing_find_primes()
        self.assertEqual(
            primes,
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        )

    def test_parallel_vs_multiprocessing(self):
        """Test shody výsledků mezi paralelním a multiprocesním vyhledáváním."""
        primes_parallel = self.prime_finder.parallel_find_primes()
        primes_multiprocessing = self.prime_finder.multiprocessing_find_primes()
        self.assertEqual(primes_parallel, primes_multiprocessing)

    def test_large_range_parallel(self):
        """Test paralelního hledání ve větším rozsahu."""
        large_prime_finder = PrimeFinder(0, 1000, 10)
        primes = large_prime_finder.parallel_find_primes()
        self.assertTrue(997 in primes)  # Největší prvočíslo pod 1000
        self.assertEqual(primes[0], 2)  # První musí být 2

    def test_large_range_multiprocessing(self):
        """Test multiprocesního hledání ve větším rozsahu."""
        large_prime_finder = PrimeFinder(0, 1000, 10)
        primes = large_prime_finder.multiprocessing_find_primes()
        self.assertTrue(997 in primes)  # Největší prvočíslo pod 1000
        self.assertEqual(primes[0], 2)  # První musí být 2

    def test_find_primes_non_integer_range(self):
        """Test rozsahu, kde start a end nejsou celá čísla."""
        with self.assertRaises(TypeError):
            self.prime_finder.find_primes_in_range(0.5, 10.5)

    def test_zero_threads(self):
        """Test chyby při zadání 0 vláken."""
        with self.assertRaises(ValueError):
            PrimeFinder(0, 100, 0)

    def test_negative_threads(self):
        """Test chyby při záporném počtu vláken."""
        with self.assertRaises(ValueError):
            PrimeFinder(0, 100, -5)

    def test_empty_range_parallel(self):
        """Test prázdného rozsahu pro paralelní hledání."""
        empty_prime_finder = PrimeFinder(20, 20, 2)
        self.assertEqual(empty_prime_finder.parallel_find_primes(), [])

    def test_empty_range_multiprocessing(self):
        """Test prázdného rozsahu pro multiprocesní hledání."""
        empty_prime_finder = PrimeFinder(20, 20, 2)
        self.assertEqual(empty_prime_finder.multiprocessing_find_primes(), [])

    def test_one_value_range(self):
        """Test rozsahu obsahujícího pouze jedno číslo."""
        self.assertEqual(self.prime_finder.find_primes_in_range(13, 13), [13])

    def test_large_prime_check(self):
        """Test na velké prvočíslo."""
        self.assertTrue(self.prime_finder.is_prime(104729))  # 10000. prvočíslo

    def test_negative_range(self):
        """Test záporného rozsahu."""
        self.assertEqual(self.prime_finder.find_primes_in_range(-10, -1), [])

    def test_non_prime_large_number(self):
        """Test velkého neprvočísla."""
        self.assertFalse(self.prime_finder.is_prime(104730))  # 104730 není prvočíslo

    def test_prime_gaps(self):
        """Test rozdílů mezi prvočísly."""
        primes = self.prime_finder.find_primes_in_range(10, 50)
        gaps = [primes[i] - primes[i - 1] for i in range(1, len(primes))]
        self.assertTrue(all(gap > 0 for gap in gaps))  # Všechny rozdíly by měly být kladné

    def test_large_range(self):
        """Test finding primes in a very large range."""
        finder = PrimeFinder(1, 100000, 4)
        primes = finder.parallel_find_primes()
        self.assertEqual(len(primes), 9592)  # Known number of primes in this range

    def test_minimum_range(self):
        """Test the smallest possible range."""
        finder = PrimeFinder(0, 1, 1)
        self.assertEqual(finder.parallel_find_primes(), [])
        self.assertEqual(finder.multiprocessing_find_primes(), [])

    def test_only_primes(self):
        """Test a range with only prime numbers."""
        finder = PrimeFinder(2, 7, 2)
        expected_primes = [2, 3, 5, 7]
        self.assertEqual(finder.parallel_find_primes(), expected_primes)
        self.assertEqual(finder.multiprocessing_find_primes(), expected_primes)

    def test_range_with_no_primes(self):
        """Test a range that contains no prime numbers."""
        finder = PrimeFinder(90, 96, 3)
        self.assertEqual(finder.parallel_find_primes(), [])
        self.assertEqual(finder.multiprocessing_find_primes(), [])

    def test_single_prime_in_range(self):
        """Test a range with exactly one prime number."""
        finder = PrimeFinder(10, 11, 1)
        self.assertEqual(finder.parallel_find_primes(), [11])
        self.assertEqual(finder.multiprocessing_find_primes(), [11])

    def test_even_range(self):
        """Test a range containing only even numbers."""
        finder = PrimeFinder(100, 110, 2)
        self.assertEqual(finder.parallel_find_primes(), [101, 103, 107, 109])

    def test_large_number_of_threads(self):
        """Test using a large number of threads."""
        finder = PrimeFinder(1, 100, 50)  # More threads than range
        primes = finder.parallel_find_primes()
        expected_primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
            61, 67, 71, 73, 79, 83, 89, 97
        ]
        self.assertEqual(primes, expected_primes)

    def test_huge_range_single_thread(self):
        """Test a very large range using a single thread."""
        finder = PrimeFinder(1, 10000, 1)
        primes = finder.parallel_find_primes()
        self.assertEqual(len(primes), 1229)  # Known number of primes in this range

    def test_huge_range_multiple_threads(self):
        """Test a very large range using multiple threads."""
        finder = PrimeFinder(1, 10000, 8)
        primes = finder.parallel_find_primes()
        self.assertEqual(len(primes), 1229)  # Same as single-threaded result

    def test_prime_verification(self):
        """Test the is_prime function directly."""
        finder = PrimeFinder(0, 10, 1)
        self.assertTrue(finder.is_prime(2))
        self.assertTrue(finder.is_prime(13))
        self.assertFalse(finder.is_prime(4))
        self.assertFalse(finder.is_prime(15))

    def test_performance_parallel_vs_multiprocessing(self):
        """Test parallel and multiprocessing results are identical."""
        finder = PrimeFinder(1, 10000, 4)
        parallel_primes = finder.parallel_find_primes()
        multiprocessing_primes = finder.multiprocessing_find_primes()
        self.assertEqual(parallel_primes, multiprocessing_primes)

    def test_empty_range(self):
        """Test an empty range."""
        finder = PrimeFinder(10, 9, 2)
        self.assertEqual(finder.parallel_find_primes(), [])
        self.assertEqual(finder.multiprocessing_find_primes(), [])

    def test_huge_prime_only(self):
        """Test range with a large prime number."""
        finder = PrimeFinder(104729, 104729, 1)  # 10000th prime number
        self.assertEqual(finder.parallel_find_primes(), [104729])
        self.assertEqual(finder.multiprocessing_find_primes(), [104729])

    def test_start_greater_than_end(self):
        """Test when start is greater than end."""
        with self.assertRaises(ValueError):
            PrimeFinder(100, 10, 2)

    def test_num_threads_validation(self):
        """Test invalid number of threads."""
        with self.assertRaises(ValueError):
            PrimeFinder(1, 10, 0)  # Zero threads
        with self.assertRaises(ValueError):
            PrimeFinder(1, 10, -1)  # Negative threads

    def test_invalid_range(self):
        """Test invalid range inputs."""
        with self.assertRaises(ValueError):
            PrimeFinder(-10, 10, 2)  # Start is negative
        with self.assertRaises(ValueError):
            PrimeFinder(-10, -5, 2)  # Entire range is negative

    def test_threads_greater_than_range(self):
        """Test more threads than numbers in range."""
        finder = PrimeFinder(10, 12, 5)  # 5 threads for range of 3
        self.assertEqual(finder.parallel_find_primes(), [11])
        self.assertEqual(finder.multiprocessing_find_primes(), [11])

    def test_large_range_primes(self):
        """Test primes in a large range."""
        finder = PrimeFinder(5000, 5100, 4)
        primes = finder.parallel_find_primes()
        expected_primes = [5003, 5009, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, 5099]
        self.assertEqual(primes, expected_primes)

    def test_invalid_data_types(self):
        """Test passing invalid data types."""
        with self.assertRaises(TypeError):
            PrimeFinder("a", 100, 4)  # Start is not an integer
        with self.assertRaises(TypeError):
            PrimeFinder(1, "b", 4)  # End is not an integer
        with self.assertRaises(TypeError):
            PrimeFinder(1, 100, "threads")  # Threads is not an integer

    def test_large_range(self):
        """Test finding primes in a very large range."""
        finder = PrimeFinder(1, 100000, 4)
        primes = finder.parallel_find_primes()
        self.assertTrue(len(primes) > 0, "Large range test failed: no primes found.")

    def test_threads_greater_than_range(self):
        """Test when number of threads exceeds the range."""
        finder = PrimeFinder(10, 15, 10)
        primes = finder.parallel_find_primes()
        self.assertEqual(primes, [11, 13], "Threads greater than range test failed.")

    def test_minimum_and_maximum_values(self):
        """Test edge cases at minimum and maximum of the range."""
        finder = PrimeFinder(0, 1, 2)
        primes = finder.parallel_find_primes()
        self.assertEqual(primes, [], "Minimum range test failed.")

        finder = PrimeFinder(1, 2, 2)
        primes = finder.parallel_find_primes()
        self.assertEqual(primes, [2], "Maximum range test failed.")

    def test_large_inputs(self):
        """Test very large inputs to ensure stability."""
        finder = PrimeFinder(99991, 100001, 4)
        primes = finder.parallel_find_primes()
        self.assertIn(99991, primes, "Large input test failed for 99991.")
        self.assertIn(100003, finder.find_primes_in_range(100000, 100005), "Large input test failed for 100003.")

    def test_parallelization_correctness(self):
        """Test correctness of threading vs multiprocessing results."""
        finder = PrimeFinder(1, 1000, 4)
        thread_primes = finder.parallel_find_primes()
        process_primes = finder.multiprocessing_find_primes()
        self.assertEqual(thread_primes, process_primes, "Parallelization correctness test failed.")

    def test_sequential_vs_parallel(self):
        """Test results between sequential and parallel calculations."""
        finder = PrimeFinder(1, 100, 4)
        sequential_primes = finder.find_primes_in_range(1, 100)
        parallel_primes = finder.parallel_find_primes()
        self.assertEqual(sequential_primes, parallel_primes, "Sequential vs Parallel test failed.")

    def test_small_prime_boundaries(self):
        """Test handling of small prime boundaries."""
        finder = PrimeFinder(1, 10, 2)
        primes = finder.parallel_find_primes()
        self.assertEqual(primes, [2, 3, 5, 7], "Small prime boundaries test failed.")
if __name__ == "__main__":
    unittest.main()
