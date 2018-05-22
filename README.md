# maze-solver
Solves a grid-based maze problem using depth-first search (stackmaze.py) and breadth-first search (queuemaze.py) strategies.

Purpose

    This program drives two solutions to a grid-based maze game using
    the Player and Position classes, relying on an array-based stack 
    and an array-based queue to store player position and allow for 
    backtracking from dead ends.

Input

    This program takes a text description of a maze as an input ("maze.txt").

Output

    After converting the text maze input to a grid representing the maze,
    this program solves the maze, printing the number of choice points
    faced by the player for the stack-based and queue-based solvers.

Bugs or Implemented Test Cases

    Without more mazes to test the stack and queue based maze solvers on,
    it is difficult to conclude anything from the Choice Point results
    obtained with each solver.  While the stack based solver encountered
    15 choice points and the queue based solver encountered 16, this difference
    may be trivial.  

    My suspicion is that it is trivial for random mazes.  Because I have used 
    breadcrumb characters to mark previously explored paths, the number of choice 
    points is driven by the number of paths explored and intersections exhausted, 
    and my suspicion is that  this number is not related to the order in which stored 
    intersections are revisited from stack or queue, even though one more path has 
    been explored in the queue-based solver than the stack-based solver in this maze.

    Because the first intersections stored in the stack are the last retrieved,
    a worst case scenario for the stack-based solver is a maze that drives the player
    through along series of intersections to a dead end deep in the maze, from which
    the solver will have to work back to a good path early in the maze.  

    Because with a queue the first intersections stored are the first revisited, 
    a worst case scenario for the queue-based solver is a maze with a good path deep 
    in the maze, past dead end intersections that the solver must explore
    before reaching the good path.  

Ben Mackenzie
Mar 8, 2018
