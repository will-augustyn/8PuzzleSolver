#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: William Augustyn
# email: will04@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, depth_limit):
        """constructs a searcher object"""
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def add_state(self, new_state):
        """adds a state to search"""
        self.states.append(new_state)
        
    def should_add(self, state):
        """determines if a state should be added"""
        if self.depth_limit == -1:
            if state.creates_cycle() == True:
                return False 
        else:
            if state.num_moves > self.depth_limit:
                return False 
            elif state.creates_cycle() == True:
                return False 
        return True 
        
    def add_states(self, new_states):
        """"adds states to searcher state list"""
        for state in new_states:
            if self.should_add(state) == True:
                self.add_state(state)
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """finds the solution to the puzzle"""
        self.add_state(init_state)
        while self.states != []:
            s = self.next_state()
            if s.is_goal() == True: 
                self.num_tested += 1
                return s
            else:
                succ = s.generate_successors()
                new_states = []
                for state in succ:
                    if self.should_add(state) == True:
                        new_states.append(state)
                self.add_states(new_states)
                self.num_tested += 1
        return None
        
        
        
    
### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """performs breadth first search"""
    def next_state(self):
        """returns the next state to be tested"""
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    """depth first search class"""
    def next_state(self):
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h2(state):
    """returns how mnay moves each tile is away from completion"""
    return state.board.moves_away()

def h1(state):
    """returns how many moves are needed to get to goal state"""
    return state.board.num_misplaced()

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    
    def __init__(self, heuristic):
        super().__init__(-1)
        self.heuristic = heuristic
        
    def add_state(self, state):
        """adds a state to be tested"""
        priority = self.priority(state)
        self.states.append([priority, state])
    
    def next_state(self):
        """finds the next state to be checked"""
        s = max(self.states)
        self.states.remove(s)
        return s[1]
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """class for Astar searcher"""
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)












