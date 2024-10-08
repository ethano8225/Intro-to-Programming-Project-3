from tkinter import *
from Pixel import Pixel
import time, random
import numpy as np

class Tetrominoes:
    def __init__(self, canvas, nrow, ncol, scale, color=2, patterns=None):
        self.canvas = canvas
        self.nrow = nrow
        self.ncol = ncol
        self.scale = scale      #set all required variables to their appropriate values
        self.color = color
        print(patterns)
        if patterns is None:
            patterns = [np.array([[2, 2, 2], [2, 0, 2], [2, 2, 2]], dtype=int)]

        self.patterns = patterns            #set the default pattern if no patterns are present
        self.nbpattern = len(self.patterns)
        self.h, self.w = self.patterns[0].shape
        self.name = "Basic"
        self.i = 0
        self.j = 0  
        self.current_pattern = 0
        self.pixels = []

    def activate(self, i=None, j=None):
        self.i = i if i is not None else 0
        self.j = j if j is not None else random.randint(0, self.ncol - self.w)
        self.pixels = []
        for i in range(self.h):         #"activate" the tetrimonoes by putting them on the window
            for j in range(self.w):
                if self.patterns[self.current_pattern][i][j] != 0:
                    pixel = Pixel(self.canvas, self.i + i, self.j + j, self.nrow, self.ncol, self.scale, self.color)
                    self.pixels.append(pixel)

    def delete(self):
        for pixel in self.pixels:       #delete pixel(s) if they are called
            pixel.delete()

    def rotate(self):
        self.current_pattern = (self.current_pattern + 1) % self.nbpattern
        self.delete()
        self.activate(self.i, self.j)       #this simply rotates the tetrimono

    def up(self):
        self.i -= 1
        self.delete()       #this moves the tetrimono up
        self.activate(self.i, self.j)

    def down(self):
        self.i += 1
        self.delete()       #this moves the tetrimono down
        self.activate(self.i, self.j)

    def left(self):
        self.j -= 1
        self.delete()       #... moves it left
        self.activate(self.i, self.j)

    def right(self):
        self.j += 1
        self.delete()       #... moves it right
        self.activate(self.i, self.j)
    
    def get_pattern(self):
        return self.patterns[self.current_pattern]

    @staticmethod
    def random_select(canv,nrow,ncol,scale):
        t1=TShape(canv,nrow,ncol,scale)
        t2=TripodA(canv,nrow,ncol,scale)
        t3=TripodB(canv,nrow,ncol,scale)        #selects a random tetrimono from the list
        t4=SnakeA(canv,nrow,ncol,scale)
        t5=SnakeB(canv,nrow,ncol,scale)
        t6=Cube(canv,nrow,ncol,scale)
        t7=Pencil(canv,nrow,ncol,scale)        
        return random.choice([t1,t2,t3,t4,t5,t6,t7,t7])
        
#########################################################
############# All Child Classes #########################
#########################################################

class TShape(Tetrominoes):
    def __init__(self, canvas, nrow, ncol, scale):
        patterns = [
            np.array([[0, 1, 0], [0, 1, 0], [1, 1, 1]], dtype=int),
            np.array([[1, 0, 0], [1, 1, 1], [1, 0, 0]], dtype=int),
            np.array([[1, 1, 1], [0, 1, 0], [0, 1, 0]], dtype=int),     #all child classes have the same idea, 
            np.array([[0, 0, 1], [1, 1, 1], [0, 0, 1]], dtype=int)      #set patterns for the specific tetromino
        ]                                                              # and inherit from Tetrimono using super
        super().__init__(canvas, nrow, ncol, scale, color=3, patterns=patterns)
        self.name = "TShape"

class TripodA(Tetrominoes):
    def __init__(self, canvas, nrow, ncol, scale):
        patterns = [
            np.array([[0,2,0], [0,2,0], [2,0,2]], dtype=int),
            np.array([[2,0,0], [0,2,2], [2,0,0]], dtype=int),
            np.array([[2,0,2], [0,2,0], [0,2,0]], dtype=int),           #function stated above
            np.array([[0,0,2], [2,2,0], [0,0,2]], dtype=int)
        ]
        super().__init__(canvas, nrow, ncol, scale, color=4, patterns=patterns)
        self.name = "TripodA"

class TripodB(Tetrominoes):
    def __init__(self, canvas, nrow, ncol, scale):
        patterns = [
            np.array([[0, 1, 0], [1, 0, 1], [1, 0, 1]], dtype=int),
            np.array([[1, 1, 0], [0, 0, 1], [1, 1, 0]], dtype=int),
            np.array([[1, 0, 1], [1, 0, 1], [0, 1, 0]], dtype=int),     #function stated above
            np.array([[0, 1, 1], [1, 0, 0], [0, 1, 1]], dtype=int)
        ]
        super().__init__(canvas, nrow, ncol, scale, color=5, patterns=patterns)
        self.name = "TripodB"

class SnakeA(Tetrominoes):
    def __init__(self, canvas, nrow, ncol, scale):
        patterns = [
            np.array([[1, 1, 0], [0, 1, 0], [0, 1, 1]], dtype=int),
            np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]], dtype=int)     #function stated above
        ]
        super().__init__(canvas, nrow, ncol, scale, color=6, patterns=patterns)
        self.name = "SnakeA"

class SnakeB(Tetrominoes):
    def __init__(self, canvas, nrow, ncol, scale):
        patterns = [
            np.array([[0, 1, 1], [0, 1, 0], [1, 1, 0]], dtype=int),      #function stated above
            np.array([[1, 0, 0], [1, 1, 1], [0, 0, 1]], dtype=int)
        ]
        super().__init__(canvas, nrow, ncol, scale, color=7, patterns=patterns)
        self.name = "SnakeB"

class Cube(Tetrominoes):
    def __init__(self, canvas, nrow, ncol, scale):
        patterns = [
            np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=int),       #function stated above
            np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=int),
            np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=int)
        ]
        super().__init__(canvas, nrow, ncol, scale, color=8, patterns=patterns)
        self.name = "Cube"

class Pencil(Tetrominoes):
    def __init__(self, canvas, nrow, ncol, scale):
        patterns = [
            np.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]], dtype=int),
            np.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]], dtype=int),       #function stated above
            np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]], dtype=int),
            np.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]], dtype=int)
        ]
        super().__init__(canvas, nrow, ncol, scale, color=9, patterns=patterns)
        self.name = "Pencil"

#########################################################
############# Testing Functions #########################
#########################################################

def delete_all(canvas):
    canvas.delete("all")
    print("Delete All")

def test1(canvas,nrow,ncol,scale):
    print("Generate a Tetromino (basic shape)- different options")
    
    tetro1=Tetrominoes(canvas,nrow,ncol,scale) # instantiate
    print("Tetro1",tetro1.name)
    print("  number of patterns:",tetro1.nbpattern)
    print("  current pattern:\n",tetro1.get_pattern()) # get current pattern
    print("  height/width:",tetro1.h,tetro1.w)
    tetro1.activate(nrow//2,ncol//2)        # activate and put on the grid
    print("  i/j coords:  ",tetro1.i,tetro1.j)

    pattern=np.array([[0,3,0],[3,3,3],[0,3,0],[3,0,3],[3,0,3]]) # set the pattern for test1
    tetro2=Tetrominoes(canvas,nrow,ncol,scale,3,[pattern]) # instantiate (list of patterns)
    print("\nTetro2",tetro2.name)
    print("  number of patterns:",tetro2.nbpattern)
    print("  current pattern:\n",tetro2.get_pattern()) # get current pattern
    print("  height/width:",tetro2.h,tetro2.w)
    tetro2.activate()        # activate and place randomly at the top of the screen
    print("  i/j coords:  ",tetro2.i,tetro2.j)
    
def test2(root,canvas,nrow,ncol,scale):
    print("Generate a 'square' Tetromino (with double shape) and rotate")
    
    print("My Tetro")
    pattern1=np.array([[4,0,0],[0,4,0],[0,0,4]]) # set the patters for this test
    pattern2=np.array([[0,0,4],[0,4,0],[4,0,0]])
    tetro=Tetrominoes(canvas,nrow,ncol,scale,4,[pattern1,pattern2]) # instantiate (list of patterns)
    print("  number of patterns:",tetro.nbpattern)
    print("  height/width:",tetro.h,tetro.w)
    tetro.activate(nrow//2,ncol//2)        # activate and place randomly at the top of the screen
    print("  i/j coords:  ",tetro.i,tetro.j)

    for k in range(10):         # make 10 rotations using a for loop
        tetro.rotate()          
        print("  current pattern:\n",tetro.get_pattern()) # retrieve current pattern
        root.update()
        time.sleep(0.5)
    tetro.delete() # delete tetro (delete every pixels)

def rotate_all(tetros):     #rotate all of tetros present
    for t in tetros:
        t.rotate()
       
def test3(root,canvas,nrow,ncol,scale):
    print("Dancing Tetrominoes")

    t0=Tetrominoes(canvas,nrow,ncol,scale)
    t1=TShape(canvas,nrow,ncol,scale)
    t2=TripodA(canvas,nrow,ncol,scale)
    t3=TripodB(canvas,nrow,ncol,scale)
    t4=SnakeA(canvas,nrow,ncol,scale)
    t5=SnakeB(canvas,nrow,ncol,scale)
    t6=Cube(canvas,nrow,ncol,scale)
    t7=Pencil(canvas,nrow,ncol,scale)       # make em' dance!
    tetros=[t0,t1,t2,t3,t4,t5,t6,t7]        # this just sets tetros to these patterns 

    for t in tetros:
        print(t.name)

                                    # place the tetrominos
    for i in range(4):
        for j in range(2):
            k=i*2+j
            tetros[k].activate(5+i*10,8+j*10)
            
    ####### Tkinter binding for this test
    root.bind("<space>",lambda e:rotate_all(tetros))     
      
def test4(root,canvas,nrow,ncol,scale):
    print("Moving Tetromino")
    tetro=Tetrominoes.random_select(canvas,nrow,ncol,scale) # choose at random
    print(tetro.name)
        
    ####### Tkinter binding for this test
    root.bind("<space>",lambda e:tetro.rotate())
    root.bind("<Up>",lambda e:tetro.up())
    root.bind("<Down>",lambda e:tetro.down())
    root.bind("<Left>",lambda e:tetro.left())
    root.bind("<Right>",lambda e:tetro.right())

    tetro.activate()

#########################################################
############# Main code #################################
#########################################################

def main():
    
    ##### create a window, canvas 
    root = Tk() # instantiate a tkinter window
    nrow=45
    ncol=30
    scale=20
    canvas = Canvas(root,width=ncol*scale,height=nrow*scale,bg="black") # create a canvas width*height
    canvas.pack()

    ### general binding events to choose a testing function
    root.bind("1",lambda e:test1(canvas,nrow,ncol,scale))
    root.bind("2",lambda e:test2(root,canvas,nrow,ncol,scale))
    root.bind("3",lambda e:test3(root,canvas,nrow,ncol,scale))
    root.bind("4",lambda e:test4(root,canvas,nrow,ncol,scale))
    root.bind("<d>",lambda e:delete_all(canvas))
    root.mainloop() # wait until the window is closed        

if __name__=="__main__":
    main()