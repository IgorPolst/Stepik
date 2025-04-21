class PowerOf:
    def __init__ (self, number):
        self.number = number
        self.counter = -1
    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter +=1
        return pow(self.number, self.counter)