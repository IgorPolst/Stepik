class Square:
    def __init__(self,n):
        self.n = n
        self.num = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n == 0:
            raise StopIteration
        
        self.num +=1
        self.n -=1
        value = pow(self.num, 2)
        return value
        

