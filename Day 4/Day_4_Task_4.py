#Implementing iter and next

class CustomImplementation:

    def __init__(self,sequence):
        self.sequence = sequence

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < len(self.sequence):
            result = sequence[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration



sequence = [1,2,3,4]
test = CustomImplementation(sequence)

i = iter(test)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

