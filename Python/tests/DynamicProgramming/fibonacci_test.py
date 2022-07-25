import timeit
import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.fibonacci import FibonacciTopDown, FibonacciBottomUp, FibonacciMemoized


class TestFibonacciAlgorithms(TestCase):

    def setUp(self) -> None:
        self.top_down = FibonacciTopDown()
        self.bottom_up = FibonacciBottomUp()
        self.memoized = FibonacciMemoized()

    def test_fibonacci_equalities(self):
        f1 = self.top_down.fib(10)
        f2 = self.bottom_up.fib(10)
        f3 = self.memoized.fib(10)
        self.assertEquals(f1, f2)
        self.assertEquals(f2, f3)

    def test_fibonacci_timings(self):
        t1 = timeit.timeit(lambda: self.top_down.fib(15), number=10000)
        t2 = timeit.timeit(lambda: self.bottom_up.fib(15), number=10000)
        t3 = timeit.timeit(lambda: self.memoized.fib(15), number=10000)
        self.assertGreater(t1, t2)
        self.assertGreater(t1, t3)


if __name__ == '__main__':
    unittest.main()
