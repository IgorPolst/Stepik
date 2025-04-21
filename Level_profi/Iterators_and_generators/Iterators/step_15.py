class Fibonacci:
    def __init__ (self):
        self.num_list = []

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.num_list) == 0:
            self.num_list.append(1)
            return 1
        elif len(self.num_list) == 1:
            self.num_list.append(1)
            return 1
        else:
            new_num = self.num_list[-1] + self.num_list[-2]
            self.num_list.append(new_num)
            return new_num
            