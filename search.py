# search.py

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
        
    return fs(problem, 1)
    
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
   
    return fs(problem, 0)

def fs(problem, tipo):
    if tipo == 1:
        from util import Stack as estr
    elif tipo == 0:
        from util import Queue as estr
    
    #inicializamos valores
    borde = estr()     
    visitado = []   
    sol = []   
    caminos = estr() 
      
    #damos los primeros valores
    borde.push(problem.getStartState())
    
    
    while not borde.isEmpty():
        
        actual = borde.pop()
        if problem.isGoalState(actual):
            break
        
        if actual not in visitado:
            #visitamos
            visitado.append(actual)
            #obtenemos todos los posibles movimientos
            successors = problem.getSuccessors(actual)
            for coord,dire,_ in successors:
                borde.push(coord)
                camino = sol + [dire]
                caminos.push(camino)
        #guardamos la solución parcial
        sol = caminos.pop()
        
    return sol

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    #inicializamos valores
    borde = util.PriorityQueue()     
    visitado = []   
    sol = []   
    caminos = util.PriorityQueue()  
      
    #damos los primeros valores
    borde.push(problem.getStartState(),0)
    
    
    while not borde.isEmpty():
        
        actual = borde.pop()
        if problem.isGoalState(actual):
            break
        
        if actual not in visitado:
            #visitamos
            visitado.append(actual)
            #obtenemos todos los posibles movimientos
            successors = problem.getSuccessors(actual)
            for coord,dire,_ in successors:
                camino = sol + [dire]
                coste = problem.getCostOfActions(camino)
                borde.push(coord, coste)
                caminos.push(camino, coste)
        #guardamos la solución parcial
        sol = caminos.pop()
        
    return sol

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #inicializamos valores
    borde = util.PriorityQueue()     
    visitado = []   
    sol = []   
    caminos = util.PriorityQueue()  
      
    #damos los primeros valores
    borde.push(problem.getStartState(),0)
    
    
    while not borde.isEmpty():
        
        actual = borde.pop()
        if problem.isGoalState(actual):
            break
        
        if actual not in visitado:
            #visitamos
            visitado.append(actual)
            #obtenemos todos los posibles movimientos
            successors = problem.getSuccessors(actual)
            for coord,dire,_ in successors:
                camino = sol + [dire]
                coste = problem.getCostOfActions(camino) + heuristic(coord,problem)
                borde.push(coord, coste)
                caminos.push(camino, coste)
        #guardamos la solución parcial
        sol = caminos.pop()
        
    return sol


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
