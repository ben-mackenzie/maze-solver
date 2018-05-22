"""
File: arrayqueue.py
"""

from arrays import Array
from abstractcollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 20

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Initalize self._front and self._rear here
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        self._front = 0
        self._rear = 0
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        pass
    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        return self._items[self._front]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        if len(self._items) == self._size:
            #resize array
            newArr = Array(self._size * 2)
            for item in self._items:
                newArr.append(item)
            self._items = newArr
        self._items[self._rear] = item
        if self._rear == len(self._items) - 1:
            self._rear = 0
            self._rear += 1
        else:
            self._rear += 1
        self._size += 1
            
    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        item = self._items[self._front]    
        if self._front == len(self._items) - 1:
            self._front = 0
        else:
            self._front += 1
        self._size -= 1
        return item   
         
