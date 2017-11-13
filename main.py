from enum import Enum
import random


class Bomb(Enum):
    NO = 0
    YES = 1


class Board:
    """
    Needs to show states of board
    * Spaces are array of (string of charactes, bomb state, nearby bombs)
    '[ ]' empty unknown
    '< >' empty known
    '<2>' 2 nearby bombs
    """
    def __init__(self, size_x, size_y, num_bombs):
        """
        Creates a game board for minesweeper
        :param size_x: Width of the board
        :param size_y: Height of the board
        :param num_bombs: Number of bombs to place
        """
        self.__spaces = [[['[ ]', Bomb.NO, 0] for col in range(size_x)] for row in range(size_y)]
        self.__filled = set()
        self._x = size_x
        self._y = size_y
        self.is_over = False
        
        for i in range(num_bombs):
            rand_x = random.randrange(0, self._x)
            rand_y = random.randrange(0, self._y)
            self.__spaces[rand_y][rand_x][1] = Bomb.YES

    def print_board(self):
        for row in self.__spaces:
            for space in row:
                print(space[0], end='')
            print()
            
    def reveal_board(self):
        for row in self.__spaces:
            for space in row:
                print(space[0][0]+str(space[1])+space[0][2], end='')
            print()
            
    def valid_space(self, x, y):
        if 0 <= x < self._x and 0 <= y < self._y:
            return True
        return False
            
    def fill_nearby(self, x, y):
        
        if not self.valid_space(x, y):
            return
        
        self.flip_space(x, y)
        self.__filled.add((x, y))
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (x+i, y+j) in self.__filled and self.nearby_bombs(x+i, y+j) == 0 \
                        and self.valid_space(x+i, y+j):
                    # print((x+i, y+j))
                    self.fill_nearby(x+i, y+j)

    def flip_space(self, x, y):
        
        if not self.valid_space(x, y):
            return
        
        space = self.__spaces[y][x]
        space[2] = self.nearby_bombs(x, y)
        
        if space[1] == Bomb.YES:
            self.is_over = True
            
        if space[0] == '[ ]':
            space[0] = '<' + str(space[2]) + '>'
            
    def nearby_bombs(self, x, y):
        if 0 <= x < self._x and 0 <= y < self._y and self.__spaces[y][x][1] == Bomb.YES:
            return "B"
        tot = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= (x + i) < self._x and 0 <= (y + j) < self._y:
                    if self.__spaces[y+j][x+i][1] == Bomb.YES:
                        tot += 1
        return tot
        

def main():
    gameboard = Board(10, 10, 10)
    
    while not gameboard.is_over:
        x, y = (int(i) for i in input("Coordinates (x,y): ").split(','))
        if x == -1 and y == -1:
            gameboard.reveal_board()
        else:
            x -= 1
            y -= 1
            gameboard.fill_nearby(x, y)
            gameboard.print_board()
        
    print("Game Over!")


main()
