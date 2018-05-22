'''
Created on Mar 9, 2018

@author: benjaminmackenzie
'''

class Intersection(object):
    '''
    The Intersection class creates intersection objects that store
    positional information about intersections encountered by the player.
    
    Class Variables:
    
    up: refers to the position above or North of the intersection's position.
    down: refers to the position below or South of the intersection's position.
    left: refers to the position to the left or West of the intersection's position.
    right: refers to the position to the right or East of the intersection's position.
    row: tracks the current row value, an integer.
    column: tracks the current column value, an integer.
    
    The up, down, left, and right status variables can have one of three values: open or closed:
    
    open: the position within the maze has a value of blank and the player has not explored it.
    blocked: the position within the maze has a value other than blank.
    explored: the player has already visited the position. 
    '''


    def __init__(self, row, column):
        '''
        Constructor
        '''
        self._row = row
        self._column = column
        self._left = [self._row, self._column - 1]
        self._right = [self._row, self._column + 1]
        self._up = [self._row - 1, self._column]
        self._down = [self._row + 1, self._column]
        self._activePath = None #tracks the last path traversed equal to left, right, up, or down
    
    def getActivePath(self):
        return self._activePath
    
    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right
    
    def getUp(self):
        return self._up
    
    def getDown(self):
        return self._down
    
    def getRow(self):
        return self._row
    
    def getColumn(self):
        return self._column 
        
    def setActivePath(self, position):
        '''tracks the trailhead position of the current path under exploration in the format [row, column]'''
        self._activePath = position
        
        