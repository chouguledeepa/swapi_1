import random


class produce_char(stat=1, stop=83):
    def __init__(self, start, stop):
        """
        Generator using random number
        :param start:
        :param stop:
        """
        self.start = start
        self.stop = stop

    def __iter__(self):
        current = self.start
        while current < 15:
            yield random.randrange(self.start, self.stop)
            current += 1
