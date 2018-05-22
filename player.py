'''
Created on Mar 9, 2018

@author: benjaminmackenzie
'''

class Player(object):
    '''
    The player class creates a player object that contains data about player position
    and methods to move the player up, down, left, and right.
    
    Class Variables:
    _current: stores the current position of the player within the maze.
    _last: stores the last position of the player before the current.
    _row: stores the current row in the grid
    _column: stores the current column in the grid
    _grid: refers to the maze grid
    
    Class Methods:
    moveUp: moves the player up one position.
    moveDown: moves the player down one position.
    moveLeft: moves the player left one position.
    moveRight: moves the player right one position.
    set and get methods for row and column, and
    get methods for current and last are also present.
    '''


    def __init__(self, grid, row = 0, column = 0):
        '''
        Sets default row and column values of 0 if none are specified.
        '''
        self._grid = grid
        self._row = row
        self._column = column
        self._last = grid[0][0]
        self._current = [self._row, self._column]
        
    def getCurrent(self):
        return self._current
    
    def getLast(self):
        return self._last
    
    def getRow(self):
        return self._row
    
    def getColumn(self):
        return self._column
    
    def setRow(self, row):
        self._row = row
    
    def setColumn(self, column): 
        self._column = column   
    
    def moveUp(self):
        '''
        Sets the last position to the current and sets current to the position
        directly above.  Moves P to the next position.
        '''
        self._last = [self._row, self._column]
        self._row = self._row - 1
        self._current = [self._row, self._column]
        self._grid[self._row][self._column] = "P"
        self._grid[self._row + 1][self._column] = '-'
        
    def moveDown(self):
        '''
        Sets the last position to the current and sets current to the position
        directly below.  Moves P to the next position.
        '''
        self._last = [self._row, self._column]
        self._row = self._row + 1
        self._current = [self._row, self._column]
        self._grid[self._row][self._column] = "P"
        self._grid[self._row - 1][self._column] = '-'
        
    def moveLeft(self):
        '''
        Sets the last position to the current and sets current to the position
        directly to the left  Moves P to the next position.
        '''
        self._last = [self._row, self._column]
        self._column = self._column - 1
        self._current = [self._row, self._column]
        self._grid[self._row][self._column] = "P"
        self._grid[self._row][self._column + 1] = '-'
        
    def moveRight(self):
        '''
        Sets the last position to the current and sets current to the position
        directly to the right.  Moves P to the next position.
        '''
        self._last = [self._row, self._column]
        self._column = self._column + 1
        self._current = [self._row, self._column]
        self._grid[self._row][self._column] = "P"
        self._grid[self._row][self._column - 1] = '-'
        
    