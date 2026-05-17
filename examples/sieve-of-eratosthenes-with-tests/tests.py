import unittest
from primes import get_primes_up_to


def is_prime_reference(n: int) -> bool:
    if n <= 1:
        return False
        
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


class TestSieve(unittest.TestCase):

    def test_small_values(self):
        self.assertEqual(get_primes_up_to(10), [2, 3, 5, 7])

    def test_edge_cases(self):
        self.assertEqual(get_primes_up_to(0), [])
        self.assertEqual(get_primes_up_to(1), [])
        self.assertEqual(get_primes_up_to(2), [2])

    def test_known_values(self):
        self.assertEqual(
            get_primes_up_to(30),
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        )

    def test_all_results_are_prime(self):
        primes = get_primes_up_to(100)
        for p in primes:
            self.assertTrue(is_prime_reference(p))

    def test_completeness(self):
        limit = 100
        primes = get_primes_up_to(limit)

        for i in range(2, limit + 1):
            if is_prime_reference(i):
                self.assertIn(i, primes)
            else:
                self.assertNotIn(i, primes)

    def test_monotonicity(self):
        primes = get_primes_up_to(100)
        i = 1
        while i < len(primes):
            self.assertTrue(primes[i] > primes[i - 1])
            i += 1

    def test_hight_values(self):
        self.assertEqual(get_primes_up_to(100_000_000)[-1], 99_999_989)


if __name__ == "__main__":
    unittest.main()
