'''
Created on Mar 17, 2018

@author: benjaminmackenzie
'''

class Position(object):
    '''
    The position class creates a position object that stores 
    position information of a location in a grid.
    
    Class Variables:
    _row: stores the row value of the maze grid coordinate.
    _column: stores the column value of the maze grid coordinate.
    
    Class Methods:
    row: returns the value of the _row data object.
    column: returns the value of the _column data object.
    '''


    def __init__(self, r = 0, c = 0):
        '''
        Sets default row and column values of 0 if none are specified.
        '''
        self._row = r
        self._column = c
        
    def row(self):
        return self._row
    
    def column(self):
        return self._column
        
        