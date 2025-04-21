class DictItemsIterator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self
    
    def __next__(self):
        keys = self.data
        list_tuple = []
        for num_key in range(len(self.data)):
            key = keys[num_key]
            value = self.data[key]
            list_tuple.append(tuple(key, value))
        
        return list_tuple