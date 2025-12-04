class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None

    def __init__ (self):
        self._head = None
        self._size = 0

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        pass
    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        pass

    '''Remove the first occurance of value.'''
    def remove(self, value):
        pass

    '''Remove all instances of value'''
    def remove_all(self, value):
        pass

    '''Convert the list to a string and return it'''
    def __str__(self):
        pass

    '''Return an iterator for the list'''
    def __iter__(self):
        pass

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        pass

    def size(self):
        pass