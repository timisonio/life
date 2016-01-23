#!/usr/bin/python3

import subprocess as sp
import time
import sys


class Life:
    def __init__(self):
        self.rows = 24
        self.cols = 80

        # create board
        self.board = [[Cell(True
                            if i%5 != 0 else False  # make things interesting initially
        ) for i in range(self.cols)] for j in range(self.rows)]
        
    def tick(self):
        for row in range(len(self.board)):
            for col in range(self.cols):
                current_cell = self.board[row][col]
                
                # make sure we don't check non-existent cells:
                row_interval = [num for num in range(row-1, row+2) if num > 0 and num < self.rows]
                col_interval = [num for num in range(col-1, col+2) if num > 0 and num < self.cols]

                # count alive neighbors for each cell
                alive_neighbors = 0
                for row2 in row_interval:
                    for col2 in col_interval:
                        if row2 == row and col2 == col:
                            continue
                        if self.board[row2][col2].query():
                            alive_neighbors += 1

                # decide all fates before applying any
                if current_cell.query() is True:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        current_cell.set_fate("die")
                    elif alive_neighbors == 2 or alive_neighbors == 3:
                        current_cell.set_fate("live")
                else:
                    if alive_neighbors == 3:
                        current_cell.set_fate("live")

        # apply fates
        for row in range(len(self.board)):
            for col in range(self.cols):
                current_cell = self.board[row][col]
                current_cell.apply_fate()
                

    def print_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print('O' if self.board[row][col].query() is True else '.', end='')
            print()           


class Cell:
    def __init__(self, state=False):
        self.alive = state
        self.fate = None

    def apply_fate(self):
        if self.fate == "die":
            self.alive = False
        else:
            self.alive = True

    def query(self):
        return self.alive

    def set_fate(self, fate):
        self.fate = fate

        
if __name__ == "__main__":
    Life = Life()
    while True:
        Life.print_board()
        Life.tick()
        time.sleep(0.1)
        tmp = sp.call('clear',shell=True)
