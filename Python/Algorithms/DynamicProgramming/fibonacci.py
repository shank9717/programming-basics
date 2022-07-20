class FibonacciTopDown:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        else:
            return self.fib(n - 1) + self.fib(n - 2)


class FibonacciRecursion(FibonacciTopDown):
    pass


class FibonacciBottomUp:
    @staticmethod
    def fib(n: int) -> int:
        if n == 0 or n == 1:
            return n
        n2 = f = 0
        n1 = 1
        for i in range(2, n + 1):
            f = n2 + n1
            n2, n1 = n1, f

        return f


class FibonacciMemoized:
    def fib(self, n: int, dp: dict = {}) -> int:
        if n in dp:
            return dp[n]
        if n == 0 or n == 1:
            return n

        else:
            f = self.fib(n - 1, dp) + self.fib(n - 2, dp)
            dp[n] = f
            return f
