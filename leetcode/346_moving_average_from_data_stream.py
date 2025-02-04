"""346. Moving Average From Data Stream"""

from collections import deque

class MovingAverage:
    """Moving Average"""

    def __init__(self, size: int):
        """ This function initializes the variables that will be used to compute the window average"""
        self.size = size
        self.window = deque()

    def next(self, val: int) -> float:
        """ This function computes the window sum and size whilst getting rid of a item when it is over the size limit. It returns the average after each insert. """
        if len(self.window) == self.size:
            self.window.popleft()

        self.window.append(val)

        return sum(self.window) / len(self.window)


