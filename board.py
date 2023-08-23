#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: William Augustyn
# email: will04@bu.edu
# 
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        num = 0
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = digitstr[num]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
                num += 1


    ### Add your other method definitions below. ###

    def __repr__(self):
        board = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    board += '_ '
                else:
                    board += f'{self.tiles[r][c]} '
                if c == 2:
                    board += '\n'
        return board
    
    def move_blank(self, direction):
        """moves the blank in the specified direction"""
        assert(direction in ['up', 'down', 'left', 'right']), False
        moves = {'up': -1, 'down': +1, 'left': -1, 'right': +1}
        if direction in ['up', 'down']:
            new_r = self.blank_r + moves[direction]
            new_c = self.blank_c
        else:
            new_c = self.blank_c + moves[direction]
            new_r = self.blank_r
        if new_r < 0 or new_r > 2:
            return False 
        elif new_c < 0 or new_c > 2:
            return False 
        original = self.tiles[new_r][new_c]
        if direction == 'up':
            self.tiles[new_r + 1][new_c] = original
            self.tiles[new_r][new_c] = '0'
            self.blank_r = new_r
            self.blank_c = new_c
            return True
        elif direction == 'down':
            self.tiles[new_r - 1][new_c] = original
            self.tiles[new_r][new_c] = '0'
            self.blank_r = new_r
            self.blank_c = new_c
            return True
        elif direction == 'left':
            self.tiles[new_r][new_c + 1] = original
            self.tiles[new_r][new_c] = '0'
            self.blank_r = new_r
            self.blank_c = new_c
            return True
        elif direction == 'right':
            self.tiles[new_r][new_c - 1] = original
            self.tiles[new_r][new_c] = '0'
            self.blank_r = new_r
            self.blank_c = new_c
            return True
        
    def digit_string(self):
        """gives a representation of the board in digit form"""
        string = ''
        for r in range(3):
            for c in range(3):
                string += self.tiles[r][c]
        return string
        
    def copy(self):
        """makes a copy of a board"""
        return Board(self.digit_string())
        
    def num_misplaced(self):
        """returns the number of tiles that are out of place"""
        num = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != GOAL_TILES[r][c] and self.tiles[r][c] != '0':
                    num += 1
        return num
                
    def __eq__(self, o):
        """checks if two board are equal"""
        if self.tiles == o.tiles:
            return True 
        else:
            return False 
    
    def moves_away(self):
        """determines the number of moves that each number is away from 
        where it should be in GOAL TILES"""
        total = 0
        correct = {'1':[0,1], '2': [0, 2], '3':[1, 0], '4':[1, 1], '5':[1,2], '6':[2,0], '7':[2,1], '8':[2,2]}
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != '0':
                    num = self.tiles[r][c]
                    correct_row = correct[num][0]
                    correct_column = correct[num][1]
                    diff = abs(correct_row - r) + abs(correct_column - c)
                    total += diff
        return total
                
                
       
                    
                
            
        
        
        
        
        
        
        
        