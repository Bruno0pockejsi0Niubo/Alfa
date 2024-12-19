
from Alfa import PrimeFinder  # Ujistěte se, že importujete správně svou třídu


import unittest

class TestPrimeFinder(unittest.TestCase):

    def setUp(self):
        """Set up the basic environment for the tests."""
        self.prime_finder = PrimeFinder(0, 100, 4)

    def test_is_prime_basic(self):
        """Test basic prime numbers."""
        self.assertTrue(self.prime_finder.is_prime(2))
        self.assertTrue(self.prime_finder.is_prime(3))
        self.assertTrue(self.prime_finder.is_prime(5))
        self.assertTrue(self.prime_finder.is_prime(7))

    def test_is_prime_non_primes(self):
        """Test non-prime numbers."""
        self.assertFalse(self.prime_finder.is_prime(1))
        self.assertFalse(self.prime_finder.is_prime(4))
        self.assertFalse(self.prime_finder.is_prime(6))
        self.assertFalse(self.prime_finder.is_prime(9))
        self.assertFalse(self.prime_finder.is_prime(15))

    def test_is_prime_edge_cases(self):
        """Test edge cases for prime numbers."""
        self.assertFalse(self.prime_finder.is_prime(0))
        self.assertFalse(self.prime_finder.is_prime(-1))
        self.assertFalse(self.prime_finder.is_prime(-10))
        self.assertTrue(self.prime_finder.is_prime(101))

    def test_find_primes_in_small_range(self):
        """Test finding primes in a small range."""
        self.assertEqual(
            self.prime_finder.find_primes_in_range(0, 10),
            [2, 3, 5, 7]
        )

    def test_find_primes_in_large_range(self):
        """Test finding primes in a larger range."""
        self.assertEqual(
            self.prime_finder.find_primes_in_range(10, 30),
            [11, 13, 17, 19, 23, 29]
        )

    def test_find_primes_no_primes(self):
        """Test a range with no primes."""
        self.assertEqual(
            self.prime_finder.find_primes_in_range(0, 1),
            []
        )

    def test_find_primes_reverse_range(self):
        """Test an invalid range where start > end."""
        self.assertEqual(
            self.prime_finder.find_primes_in_range(20, 10),
            []
        )

    def test_parallel_find_primes(self):
        """Test parallel prime finding."""
        prime_finder_parallel = PrimeFinder(0, 50, 4)
        primes = prime_finder_parallel.parallel_find_primes()
        self.assertEqual(
            primes,
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        )

    def test_multiprocessing_find_primes(self):
        """Test multiprocessing prime finding."""
        prime_finder_multiprocess = PrimeFinder(0, 50, 4)
        primes = prime_finder_multiprocess.multiprocessing_find_primes()
        self.assertEqual(
            primes,
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        )

    def test_parallel_vs_multiprocessing(self):
        """Test consistency between parallel and multiprocessing prime finding."""
        primes_parallel = self.prime_finder.parallel_find_primes()
        primes_multiprocessing = self.prime_finder.multiprocessing_find_primes()
        self.assertEqual(primes_parallel, primes_multiprocessing)

    def test_large_range_parallel(self):
        """Test parallel prime finding in a large range."""
        large_prime_finder = PrimeFinder(0, 1000, 10)
        primes = large_prime_finder.parallel_find_primes()
        self.assertTrue(997 in primes)  # Largest prime under 1000
        self.assertEqual(primes[0], 2)  # First should be 2

    def test_large_range_multiprocessing(self):
        """Test multiprocessing prime finding in a large range."""
        large_prime_finder = PrimeFinder(0, 1000, 10)
        primes = large_prime_finder.multiprocessing_find_primes()
        self.assertTrue(997 in primes)  # Largest prime under 1000
        self.assertEqual(primes[0], 2)  # First should be 2

    def test_find_primes_non_integer_range(self):
        """Test a range where start and end are not integers."""
        with self.assertRaises(TypeError):
            self.prime_finder.find_primes_in_range(0.5, 10.5)

    def test_zero_threads(self):
        """Test error when 0 threads are specified."""
        with self.assertRaises(ValueError):
            PrimeFinder(0, 100, 0)

    def test_negative_threads(self):
        """Test error when a negative number of threads is specified."""
        with self.assertRaises(ValueError):
            PrimeFinder(0, 100, -5)

    def test_empty_range_parallel(self):
        """Test empty range for parallel prime finding."""
        empty_prime_finder = PrimeFinder(20, 20, 2)
        self.assertEqual(empty_prime_finder.parallel_find_primes(), [])

    def test_empty_range_multiprocessing(self):
        """Test empty range for multiprocessing prime finding."""
        empty_prime_finder = PrimeFinder(20, 20, 2)
        self.assertEqual(empty_prime_finder.multiprocessing_find_primes(), [])

    def test_one_value_range(self):
        """Test a range containing only one number."""
        self.assertEqual(self.prime_finder.find_primes_in_range(13, 13), [13])

    def test_large_prime_check(self):
        """Test for a large prime number."""
        self.assertTrue(self.prime_finder.is_prime(104729))  # 10000th prime

    def test_negative_range(self):
        """Test for a negative range."""
        self.assertEqual(self.prime_finder.find_primes_in_range(-10, -1), [])

    def test_non_prime_large_number(self):
        """Test a large non-prime number."""
        self.assertFalse(self.prime_finder.is_prime(104730))  # 104730 is not prime

    def test_prime_gaps(self):
        """Test gaps between prime numbers."""
        primes = self.prime_finder.find_primes_in_range(10, 50)
        gaps = [primes[i] - primes[i - 1] for i in range(1, len(primes))]
        self.assertTrue(all(gap > 0 for gap in gaps))  # All gaps should be positive

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

    def test_single_point_range(self):
        """Test where start equals end."""
        finder = PrimeFinder(11, 11, 1)
        self.assertEqual(finder.parallel_find_primes(), [11], "Single point range test failed.")

    def test_single_prime_in_range(self):
        """Test range containing a single prime number."""
        finder = PrimeFinder(13, 13, 1)
        self.assertEqual(finder.parallel_find_primes(), [13], "Single prime in range test failed.")

    def test_no_primes_in_range(self):
        """Test range with no primes."""
        finder = PrimeFinder(90, 92, 1)
        self.assertEqual(finder.parallel_find_primes(), [], "No primes in range test failed.")

    def test_single_thread(self):
        """Test calculation using a single thread."""
        finder = PrimeFinder(1, 100, 1)
        self.assertEqual(finder.parallel_find_primes(), finder.find_primes_in_range(1, 100),
                         "Single thread test failed.")

    def test_many_threads_small_range(self):
        """Test using many threads on a small range."""
        finder = PrimeFinder(1, 10, 20)
        self.assertEqual(finder.parallel_find_primes(), [2, 3, 5, 7], "Many threads small range test failed.")

    def test_large_primes_range(self):
        """Test finding large primes."""
        finder = PrimeFinder(1000000, 1000010, 2)
        self.assertIn(1000003, finder.parallel_find_primes(), "Large primes range test failed.")

    def test_large_range_with_min_threads(self):
        """Test large range with only one thread."""
        finder = PrimeFinder(1, 100000, 1)
        primes = finder.parallel_find_primes()
        self.assertTrue(len(primes) > 0, "Large range with min threads test failed.")

    def test_prime_boundary_overlap(self):
        """Test range partially overlapping primes."""
        finder = PrimeFinder(9, 13, 2)
        self.assertEqual(finder.parallel_find_primes(), [11, 13], "Prime boundary overlap test failed.")

    def test_invalid_thread_count(self):
        """Test invalid thread count."""
        with self.assertRaises(ValueError):
            PrimeFinder(1, 10, 0)

        with self.assertRaises(ValueError):
            PrimeFinder(1, 10, -1)

    def test_maximum_range_length(self):
        """Test maximum length range."""
        finder = PrimeFinder(1, 1000000, 4)
        primes = finder.parallel_find_primes()
        self.assertTrue(len(primes) > 0, "Maximum range length test failed.")

    def test_empty_range_multiple_threads(self):
        """Test empty range with multiple threads."""
        finder = PrimeFinder(10, 10, 5)
        self.assertEqual(finder.parallel_find_primes(), [], "Empty range multiple threads test failed.")

    def test_step_size_in_parallelization(self):
        """Test step sizes in parallelization."""
        finder = PrimeFinder(1, 100, 5)
        primes = finder.parallel_find_primes()
        expected = finder.find_primes_in_range(1, 100)
        self.assertEqual(primes, expected, "Step size in parallelization test failed.")

    def test_asymmetric_range(self):
        """Test highly asymmetric range with few threads."""
        finder = PrimeFinder(2, 1000000, 3)
        primes = finder.parallel_find_primes()
        self.assertTrue(len(primes) > 0, "Asymmetric range test failed.")

    def test_single_prime_range(self):
        """Test small range containing a single prime."""
        finder = PrimeFinder(2, 2, 1)
        self.assertEqual(finder.parallel_find_primes(), [2], "Single prime range test failed.")

    def test_max_threads_equal_to_range_size(self):
        """Test maximum threads equal to range size."""
        finder = PrimeFinder(1, 10, 10)
        self.assertEqual(finder.parallel_find_primes(), [2, 3, 5, 7], "Max threads equal to range size test failed.")

    def test_large_numbers_in_range(self):
        """Test range with large numbers."""
        finder = PrimeFinder(1000000, 1000020, 4)
        primes = finder.parallel_find_primes()
        self.assertTrue(1000003 in primes, "Large numbers in range test failed.")

    def test_range_with_single_number(self):
        """Test range containing only one number."""
        finder = PrimeFinder(15, 15, 1)
        self.assertEqual(finder.parallel_find_primes(), [], "Range with single number test failed.")

    def test_repeated_runs_consistency(self):
        """Test multiple executions for consistency."""
        finder = PrimeFinder(1, 100, 4)
        result1 = finder.parallel_find_primes()
        result2 = finder.parallel_find_primes()
        self.assertEqual(result1, result2, "Repeated runs consistency test failed.")

    def test_more_threads_than_range(self):
        """Test using more threads than numbers in range."""
        finder = PrimeFinder(10, 12, 10)
        self.assertEqual(finder.parallel_find_primes(), [11], "More threads than range test failed.")

    def test_boundary_values_single_thread(self):
        """Test single thread with boundary values."""
        finder = PrimeFinder(0, 1, 1)
        self.assertEqual(finder.parallel_find_primes(), [], "Boundary values single thread test failed.")

    def test_zero_range(self):
        """Test range starting and ending at zero."""
        finder = PrimeFinder(0, 0, 1)
        self.assertEqual(finder.parallel_find_primes(), [], "Zero range test failed.")

    def test_max_integer_range(self):
        """Test large range near the integer max value."""
        max_value = 2 ** 31 - 1  # Adjust as needed for practical tests
        finder = PrimeFinder(max_value - 10, max_value, 4)
        primes = finder.parallel_find_primes()
        self.assertTrue(len(primes) > 0, "Max integer range test failed.")

    def test_single_prime_range(self):
        """Test small range containing a single prime."""
        finder = PrimeFinder(2, 2, 1)
        self.assertEqual(finder.parallel_find_primes(), [2], "Single prime range test failed.")

    def test_max_threads_equal_to_range_size(self):
        """Test maximum threads equal to range size."""
        finder = PrimeFinder(1, 10, 10)
        self.assertEqual(finder.parallel_find_primes(), [2, 3, 5, 7], "Max threads equal to range size test failed.")

    def test_large_numbers_in_range(self):
        """Test range with large numbers."""
        finder = PrimeFinder(1000000, 1000020, 4)
        primes = finder.parallel_find_primes()
        self.assertTrue(1000003 in primes, "Large numbers in range test failed.")

    def test_range_with_single_number(self):
        """Test range containing only one number."""
        finder = PrimeFinder(15, 15, 1)
        self.assertEqual(finder.parallel_find_primes(), [], "Range with single number test failed.")

    def test_repeated_runs_consistency(self):
        """Test multiple executions for consistency."""
        finder = PrimeFinder(1, 100, 4)
        result1 = finder.parallel_find_primes()
        result2 = finder.parallel_find_primes()
        self.assertEqual(result1, result2, "Repeated runs consistency test failed.")

    def test_more_threads_than_range(self):
        """Test using more threads than numbers in range."""
        finder = PrimeFinder(10, 12, 10)
        self.assertEqual(finder.parallel_find_primes(), [11], "More threads than range test failed.")

    def test_boundary_values_single_thread(self):
        """Test single thread with boundary values."""
        finder = PrimeFinder(0, 1, 1)
        self.assertEqual(finder.parallel_find_primes(), [], "Boundary values single thread test failed.")

    def test_zero_range(self):
        """Test range starting and ending at zero."""
        finder = PrimeFinder(0, 0, 1)
        self.assertEqual(finder.parallel_find_primes(), [], "Zero range test failed.")

    def test_max_integer_range(self):
        """Test large range near the integer max value."""
        max_value = 2 ** 31 - 1  # Adjust as needed for practical tests
        finder = PrimeFinder(max_value - 10, max_value, 4)
        primes = finder.parallel_find_primes()
        self.assertTrue(len(primes) > 0, "Max integer range test failed.")

    def test_small_range_with_one_prime(self):
        """Test a small range with one prime number."""
        finder = PrimeFinder(10, 11, 2)
        self.assertEqual(finder.parallel_find_primes(), [11], "Small range with one prime test failed.")

    def test_large_range_with_primes_on_edges(self):
        """Test a large range with prime numbers on the edges."""
        finder = PrimeFinder(89, 97, 3)
        self.assertEqual(finder.parallel_find_primes(), [89, 97], "Large range with primes on edges test failed.")

    def test_range_with_all_primes(self):
        """Test a range where all numbers are prime."""
        finder = PrimeFinder(2, 7, 2)
        self.assertEqual(finder.parallel_find_primes(), [2, 3, 5, 7], "Range with all primes test failed.")

    def test_minimal_range_non_prime(self):
        """Test a minimal range with a single non-prime number."""
        finder = PrimeFinder(4, 4, 1)
        self.assertEqual(finder.parallel_find_primes(), [], "Minimal range non-prime test failed.")

    def test_minimal_range_prime(self):
        """Test a minimal range with a single prime number."""
        finder = PrimeFinder(13, 13, 1)
        self.assertEqual(finder.parallel_find_primes(), [13], "Minimal range prime test failed.")

    def test_large_range_with_many_primes(self):
        """Test a large range with many small primes."""
        finder = PrimeFinder(0, 50, 4)
        self.assertEqual(
            finder.parallel_find_primes(),
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
            "Large range with many primes test failed."
        )

    def test_single_prime_two(self):
        """Test a range containing only the smallest prime (2)."""
        finder = PrimeFinder(2, 2, 1)
        self.assertEqual(finder.parallel_find_primes(), [2], "Single prime two test failed.")

    def test_large_primes_range(self):
        """Test a range containing very large prime numbers."""
        finder = PrimeFinder(997, 1009, 4)
        self.assertEqual(finder.parallel_find_primes(), [997, 1009], "Large primes range test failed.")

    def test_all_single_digit_primes(self):
        """Test a range containing all single-digit prime numbers."""
        finder = PrimeFinder(0, 10, 2)
        self.assertEqual(finder.parallel_find_primes(), [2, 3, 5, 7], "All single-digit primes test failed.")

    def test_range_ending_at_square_root(self):
        """Test a range where the end is a square root of a perfect square."""
        finder = PrimeFinder(15, 16, 2)
        self.assertEqual(finder.parallel_find_primes(), [], "Range ending at square root test failed.")

    def test_first_three_double_digit_primes(self):
        """Test a range containing the first three double-digit primes."""
        finder = PrimeFinder(11, 17, 2)
        self.assertEqual(finder.parallel_find_primes(), [11, 13, 17], "First three double-digit primes test failed.")

    def test_range_with_large_near_prime(self):
        """Test a range containing a large number close to a prime."""
        finder = PrimeFinder(98, 101, 2)
        self.assertEqual(finder.parallel_find_primes(), [101], "Range with large near prime test failed.")

    def test_maximum_threads(self):
        """Test using a very high number of threads for a small range."""
        finder = PrimeFinder(2, 10, 1000)
        self.assertEqual(finder.parallel_find_primes(), [2, 3, 5, 7], "Maximum threads test failed.")

    def test_no_primes_in_range(self):
        """Test a range that contains no prime numbers."""
        finder = PrimeFinder(90, 96, 2)
        self.assertEqual(finder.parallel_find_primes(), [], "No primes in range test failed.")

    def test_single_large_prime(self):
        """Test a range containing exactly one large prime."""
        finder = PrimeFinder(10007, 10007, 1)
        self.assertEqual(finder.parallel_find_primes(), [10007], "Single large prime test failed.")

    def test_huge_prime_gap(self):
        """Test a range containing a known large gap between primes."""
        finder = PrimeFinder(113, 127, 4)
        self.assertEqual(finder.parallel_find_primes(), [113, 127], "Huge prime gap test failed.")
if __name__ == "__main__":
    unittest.main()
