class MyIterator:
    def __init__(self, iterator):
        self.iterator = iterator

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index + 1 < len(self.iterator):
            self.index += 1
            return self.iterator[self.index]
        else:
            raise StopIteration