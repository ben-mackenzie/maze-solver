'''
Created on Apr 1, 2018

@author: benjaminmackenzie

A stack-based solver for the maze game.
'''

from grid import Grid
from arraystack import ArrayStack
from player import Player
from intersection import Intersection

def stackMaze(mazeText):
    
    #parses maze file and captures maze attributes
    mazeFile = open(mazeText, "r")
    mazeList = mazeFile.read().splitlines() #https://stackoverflow.com/questions/24946640/removing-r-n-from-a-python-list-after-importing-with-readlines
    mazeFile.close()
    rows = len(mazeList)
    columns = len(mazeList[0])
    
    #builds blank grid
    maze = Grid(rows, columns)
    
    #builds maze from list of maze rows
    for row in range(maze.getHeight()):
        for column in range(maze.getWidth()):
            maze[row][column] = mazeList[row][column]
            
    #creates intersection stack
    stack = ArrayStack()
            
    #creates a player
    player = Player(maze)
    
    #searches for starting point of player
    for r in range(0, rows):
        for c in range(0, columns):
            if maze[r][c] == "P":
                player.setRow(r)
                player.setColumn(c) 
                break           
    
    choicePoints = 0
    
    #end condition check
    while maze[player.getRow()][player.getColumn() + 1] != 'T':
            
        #convenience variables representing the value of the grid at these positions relative to player
        up = maze[player.getRow() - 1][player.getColumn()]
        down = maze[player.getRow() + 1][player.getColumn()]
        right = maze[player.getRow()][player.getColumn() + 1]
        left = maze[player.getRow()][player.getColumn() - 1]
        
        #dead end check   
        routes = 0
        if up == ' ':
            routes += 1
        if down == ' ':
            routes += 1
        if right == ' ':
            routes += 1
        if left == ' ':
            routes += 1
        if routes == 0:
            #player is at a dead end.  REWRITE BACKTRACK LOGIC
            #retrieves the previous intersection from the stack
            pos = stack.pop() 
            #backtracks the player to previous intersection
            maze[player.getRow()][player.getColumn()] = '-'
            player.setRow(pos.getRow()) 
            player.setColumn(pos.getColumn())
            maze[pos.getRow()][pos.getColumn()] = 'P'
            #marks last path as dead end
            maze[pos.getActivePath()[0]][pos.getActivePath()[1]]  = '-'
            
        elif routes > 1:
            #player is at an intersection
            #increment choice points by 1
            choicePoints += 1
            intersection = Intersection(player.getRow(), player.getColumn())
            if up == ' ':
                intersection.setActivePath([player.getRow() - 1, player.getColumn()])
                nextMove = player.moveUp()
            elif down == ' ':
                intersection.setActivePath([player.getRow() + 1, player.getColumn()])
                nextMove = player.moveDown()
            elif right == ' ':
                intersection.setActivePath([player.getRow(), player.getColumn() + 1])
                nextMove = player.moveRight()
            elif left == ' ':
                intersection.setActivePath([player.getRow(), player.getColumn() - 1])                
                nextMove = player.moveLeft()
            stack.push(intersection)        
         
        else:    
            #the player is not at a dead end
            if down == ' ':
                nextMove = player.moveDown()
            elif up == ' ':
                nextMove = player.moveUp()
            elif right == ' ':
                nextMove = player.moveRight()
            elif left == ' ':
                nextMove = player.moveLeft()
            
        #moves player to the next position
        nextMove    
            
    #moves P to the end of the maze       
    maze[player.getRow()][player.getColumn()] = "-"        
    maze[player.getRow()][player.getColumn() + 1] = "P"
    print("Stack-based Maze Solution:\n")    
    print(maze) 
    print("Choice points: " + str(choicePoints)+ "\n")
    
    #writes maze solution to text file
    fw = open("stacksolution.txt", "w")
    fw.writelines(str(maze))
    fw.write("Choice points: " + str(choicePoints) + "\n")
    fw.close()