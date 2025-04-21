class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.times > 0:
            self.times -= 1
            return self.obj
        else:
            raise (StopIteration)

