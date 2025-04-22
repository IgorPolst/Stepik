class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        el = self.iterable[self.index]
        if self.index >= len(self.iterable)-1:
            self.index = 0
        else: 
            self.index += 1
        return el
    
cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))