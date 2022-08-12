Template Method pattern that allows you to define the skeleton 
of an algorithm in a base class and let implementations decide
how some steps behave without changing the overall implementation
of the algorithm.

In the given example, we have a generic trading algorithm implementation
which first gets the current price of a stock, then has to decide whether 
to buy or sell, and finally place the order. Here, the decision can be
handled by different subclasses extending TradingAlgorithm and its implementation.
