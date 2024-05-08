from tkinter import *
from Grid import Grid
from Tetrominoes import Tetrominoes
import time

class Tetris(Grid):
    def __init__(self, root, nrow, ncol, scale):
        super().__init__(root, nrow, ncol, scale)
        self.block = None
        self.game_over = False

    def next(self):
        if self.block is None:  # If no block is active
            self.block = Tetrominoes.random_select(self.canvas, self.nrow, self.ncol, self.scale)
            self.block.activate()
        else:
            self.block.down()
            i, j = self.block.i, self.block.j

            # Check if the block is at the bottom or overlapping with another block
            if i + self.block.h >= self.nrow or self.is_overlapping(i + 1, j):
                # Block is in place
                pattern = self.block.get_pattern()
                self.block.delete()
                for r in range(self.block.h):
                    for c in range(self.block.w):
                        if pattern[r][c] != 0:
                            if i+r > 19:
                                i = 18
                            self.add_ij(i + r, j + c, pattern[r][c])
                self.flush_rows()
                self.check_game_over()

                # Reset block
                self.block = None

    def is_overlapping(self, ii, jj):
        for r in range(3):
            for c in range(3):
                if ii + r < self.nrow and jj + c < self.ncol:
                    if self.Integer[ii + r][jj + c] != 0 and self.block.patterns[self.block.current_pattern][r][c] != 0:
                        return True
        return False

    def flush_rows(self, row=0):
        row_to_flush = []
        for i in range(self.nrow):
            if 0 not in self.Integer[i]:
                row_to_flush.append(i)
        for row in row_to_flush:
            self.flush(row)

    def check_game_over(self):
        if any(self.Integer[i][j] != 0 for i in range(3) for j in range(self.ncol)):
            self.game_over = True

    def up(self):
        if self.block is not None:
            self.block.rotate()

    def down(self):
        while self.block is not None:
            self.next()

    def left(self):
        if self.block is not None:
            if self.block.j > 0:
                for r in range(self.block.h):
                    for c in range(self.block.w):
                        if self.block.patterns[self.block.current_pattern][r][c] != 0:
                            if self.is_overlapping(self.block.i + r, self.block.j + c-1):
                                return  # Don't move if overlap
                self.block.left()

    def right(self):
        if self.block is not None:
            if self.block.j + self.block.w < self.ncol:
                for r in range(self.block.h):
                    for c in range(self.block.w):
                        if self.block.patterns[self.block.current_pattern][r][c] != 0:
                            if self.is_overlapping(self.block.i + r, self.block.j + c+1):
                                return  # Don't move if overlap
                self.block.right()

#    def left(self):
#        if self.block is not None:
#            if self.block.j > 0 and not self.is_overlapping(self.block.i, self.block.j - 1):
#                self.block.left()
#
#    def right(self):
#        if self.block is not None:
#            if self.block.j + self.block.w < self.ncol and not self.is_overlapping(self.block.i, self.block.j + 1):
#                self.block.right()

# Testing the Tetris class
def main():
    root = Tk()
    tetris_game = Tetris(root, 20, 10, 30)
    
    # Bind keys for controls
    root.bind("<Up>", lambda e: tetris_game.up())
    root.bind("<Down>", lambda e: tetris_game.down())
    root.bind("<Left>", lambda e: tetris_game.left())
    root.bind("<Right>", lambda e: tetris_game.right())

    
    # Main loop
    while not tetris_game.game_over:
        tetris_game.next()
        root.update()
        time.sleep(0.5)

    root.mainloop()

if __name__ == "__main__":
    main()
