import unittest

"""Find the fibonacci number for n"""

memo = {}


def fib(n):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


class Tests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(fib(10), 55)


if __name__ == "__main__":
    unittest.main()
