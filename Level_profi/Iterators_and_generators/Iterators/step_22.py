class Xrange:

    def __init__(self, start, end, step):
        if start <= end:
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration

        res = self.start
        self.start += self.step
        return res

xrange = Xrange(10, 1, -1)

print(*xrange)
