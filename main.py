class Array:
    def __init__ (self, size, items):
        self.size = size
        if list(map(type,items)).count(list(map(type,items))[0]) == len(items) and self.size > len(items):
            self.typey = list(map(type,items))[0]
            self.array = items
        else:
            raise TypeError("Item data types do not match")
            
    def append(self, item):
        if type(item) == self.typey and len(self.array) < self.size:
            self.array.append(item)
        elif len(self.array) < self.size:
            raise OverflowError("BufferError: Overflow error")
        else:
            raise TypeError("TypeError: item data type does not match")
   
    def __getitem__ (self, index):
        return (self.array[int(index)])
    
    def __setitem__(self, index, item):
        if type(item) == self.typey:
            self.array[index] = item
        else:
            raise TypeError("TypeError: item data type does not match")

    def __repr__(self):
        return (self.array)
