
class Array:

    class Iterator:

        def __init__(self, array, position):

            self.array = array
            self.position = position

        def get_current(self):
            return self.array[self.position]

        def has_next(self):
            return (self.position + 1) < len(self.array)

        def get_next(self):
            return Array.Iterator(self.array, self.position + 1)

    def __init__(self, array):

        self._storage = array

    def get_iterator(self):

        return Array.Iterator(self, 0)
    
a = Array([1, 2, 3])

iter = a.get_iterator()

while True:

    print(iter.get_current())

    if not iter.has_next():
        break
    else:
        iter = iter.get_next()
