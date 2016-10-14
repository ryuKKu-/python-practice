import random


class QuickSort(object):
    def __init__(self, numbers):
        self.values = numbers
        self.count = len(self.values)

    def sort(self):
        self.partition(0, self.count - 1)
        return self.values

    def partition(self, begin, end):
        if begin >= end:
            return

        idx_bot, idx_top = begin, end
        pivot = self.values[random.randint(begin, end)]

        while idx_bot <= idx_top:
            while self.values[idx_bot] < pivot:
                idx_bot += 1
            while self.values[idx_top] > pivot:
                idx_top -= 1

            if idx_bot <= idx_top:
                self.values[idx_bot], self.values[idx_top] = self.values[idx_top], self.values[idx_bot]
                idx_bot, idx_top = idx_bot + 1, idx_top - 1

        self.partition(begin, idx_top)
        self.partition(idx_bot, end)
