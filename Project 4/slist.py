class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None
            self.prev = None

    def __init__ (self):
        self._head = None
        self._tail = None
        self._size = 0

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        #use a doubly linked list
        #set curr_node to a node containing value
        new_node = SList.SListNode(value)
        #if list Slist is empty insert node as head and tail
        

        if self._head is None and self._tail is None:
            self._head = new_node
            self._tail = new_node
            new_node.next = None
            new_node.prev = None
            self._size += 1
            return


        #search list for a value greater than curr_node.value
        curr_node = self._head
        while curr_node is not None and curr_node.value < value:
            curr_node = curr_node.next
        #set succ_node to that node
        succ_node = curr_node
        #set pred_node to succ_node.prev
        pred_node = None
        if succ_node is not None:
            pred_node = succ_node.prev
        else:
            pred_node = self._tail
        
        #if pred_node is None, we are at head
        #if inserting at head update head
        if pred_node is None:
            new_node.next = self._head
            new_node.prev = None
            self._head.prev = new_node
            self._head = new_node
            self._size += 1
            return
        #if succ_node is None, we are at tail
        #if inserting at tail update tail
        elif succ_node is None:
            new_node.prev = self._tail
            new_node.next = None
            self._tail.next = new_node
            self._tail = new_node
            self._size += 1
            return
        #if inserting in middle of list
        #update pointers appropriately
        else:
            new_node.prev = pred_node
            new_node.next = succ_node
            pred_node.next = new_node
            succ_node.prev = new_node
            self._size += 1
            return
    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        curr_node = self._head
        while curr_node is not None:
            if curr_node.value == value:
                return curr_node.value
            curr_node = curr_node.next
        return None

    '''Remove the first occurance of value.'''
    def remove(self, value):
        curr_node = self._head
        while curr_node is not None:
            if curr_node.value == value:
                #if node to remove is head
                if curr_node.prev is None:
                    self._head = curr_node.next
                    if self._head is not None:
                        self._head.prev = None
                    else:
                        self._tail = None
                #if node to remove is tail
                elif curr_node.next is None:
                    self._tail = curr_node.prev
                    if self._tail is not None:
                        self._tail.next = None
                    else:
                        self._head = None
                #if node to remove is in middle
                else:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                self._size -= 1
                return
            curr_node = curr_node.next

    '''Remove all instances of value'''
    def remove_all(self, value):
        curr_node = self._head
        while curr_node is not None:
            if curr_node.value == value:
                #if node to remove is head
                if curr_node.prev is None:
                    self._head = curr_node.next
                    if self._head is not None:
                        self._head.prev = None
                    else:
                        self._tail = None
                    curr_node = self._head
                #if node to remove is tail
                elif curr_node.next is None:
                    self._tail = curr_node.prev
                    if self._tail is not None:
                        self._tail.next = None
                    else:
                        self._head = None
                    curr_node = None
                #if node to remove is in middle
                else:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                    curr_node = curr_node.next
                self._size -= 1
            else:
                curr_node = curr_node.next

    '''Convert the list to a string and return it'''
    def __str__(self):
        return "[" + ", ".join(str(item) for item in self) + "]"

    '''Return an iterator for the list'''
    def __iter__(self):
        curr_node = self._head
        while curr_node is not None:
            yield curr_node.value
            curr_node = curr_node.next

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        curr_node = self._head
        for _ in range(index):
            curr_node = curr_node.next
        return curr_node.value

    def size(self):
        return self._size