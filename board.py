from colors import colored_print
from pieces import Piece

class Board:
    def __init__(self, rows : int, cols : int):
        self.rows = rows
        self.cols = cols
        self.cells = [[Piece() for row in range (self.cols)] for col in range (self.rows)]

    def draw_board(self):

        for row in range (2 * self.rows + 1):
            for col in range (self.cols):
                if row % 2 == 1:
                    if col == 0:
                        print (f"{chr (ord ('A') + row//2)}\t|", end = '')
                    num = self.cells[row//2][col].get_count()
                    if num != 0:
                        colored_print (f" {num} ", num, end_with = '')
                    else:
                        print ("   ", end = '')
                    print ('|', end = '')
                else:
                    if col == 0:
                        print ('\t|', end = '')
                    print ('---|', end = '')
            print ('')
        print ('\t ', end = '')
        for col in range (self.cols):
            print (f" {1 + col}  ", end = '')
        print ('')

    def make_play (self, row : int, col : int) -> bool:
        if not self.cells[row][col].add_piece():
            print ("Erro! ja existe um vermelho nessa posiçao!")
            return False
        return True

    def in_bounds (self, row : int, col : int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols


    def check_winner_hor (self) -> bool:
        positions = []
        for row in range (self.rows):
            level = -1
            chain = 0
            for col in range (self.cols):
                value = self.cells[row][col].get_count()
                if value != 0:
                    if level != value:
                        level = value
                        chain = 1
                        positions = []
                        positions.append ((row, col))
                    else:
                        positions.append ((row, col))
                        chain += 1
                    if chain == 3:
                        print ('winner found HOR')
                        return True
                else:
                    level = -1
                    chain = 0
        return False

    def check_winner_vert (self) -> bool:
        positions = []
        for col in range (self.cols):
            level = -1
            chain = 0
            for row in range (self.rows):
                value = self.cells[row][col].get_count()
                if value != 0:
                    if level != value:
                        level = value
                        positions = []
                        positions.append ((row,col))
                        chain = 1
                    else:
                        positions.append ((row, col))
                        chain += 1
                    if chain == 3:
                        print ('winner found VER')
                        print (positions)
                        return True
                else:
                    level = -1
                    chain = 0

        return False


    def check_winner (self):
        return self.check_winner_hor () or self.check_winner_vert ()