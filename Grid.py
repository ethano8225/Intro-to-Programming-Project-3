from tkinter import *
from Pixel import Pixel
import numpy as np
import random, time


class Grid:
    def __init__(self, root, nrow, ncol, scale):
        self.root = root
        self.canvas = Canvas(root, width=ncol*scale, height=nrow*scale, bg='black')
        self.canvas.pack()
        self.nrow = nrow
        self.ncol = ncol
        self.scale = scale
        self.pixels = []
        self.matrix = np.zeros((nrow, ncol), dtype=int)
        self.draw_gridlines()

    def draw_gridlines(self):
        for i in range(self.nrow):
            self.canvas.create_line(0, i*self.scale, self.ncol*self.scale, i*self.scale, fill="gray")
        for j in range(self.ncol):
            self.canvas.create_line(j*self.scale, 0, j*self.scale, self.nrow*self.scale, fill="gray")

    def addij(self, i, j, c):
        if c > 0:  # if color is not black
            self.matrix[i, j] = c
            pixel = Pixel(self.canvas, i, j, self.nrow, self.ncol, self.scale, colorid=c)
            self.pixels.append(pixel)

    def random_pixels(self, num_pixels, color):
        for _ in range(num_pixels):
            i = random.randint(0, self.nrow - 1)
            j = random.randint(0, self.ncol - 1)
            self.addij(i, j, color)

    def addxy(self, event):
        j = event.x // self.scale
        i = event.y // self.scale
        color = self.matrix[i, j]
        print(f"insert {event.x} {event.y} {i} {j} {color}")
        self.addij(i, j, 1)

    def delij(self, i, j):
        color = self.matrix[i, j]
        if color > 0:  # if color is not black
            self.matrix[i, j] = 0
            self.reset()
        else:
            self.flush_row(i)

    def delxy(self, event):
        j = event.x // self.scale
        i = event.y // self.scale
        color = self.matrix[i, j]
        print(f"delete {event.x} {event.y} {i} {j} {color}")
        self.delij(i, j)

    def reset(self):
        for pixel in self.pixels:
            pixel.delete()
        self.pixels.clear()
        for i in range(self.nrow):
            for j in range(self.ncol):
                if self.matrix[i, j] > 0:
                    self.addij(i, j, self.matrix[i, j])

    def flush_row(self, i):
        left = 0
        right= 29
        self.addij(i,left,7), self.addij(i,left+1,7), self.addij(i,left+2,7)     #spawn in clear row
        self.addij(i,right,7), self.addij(i,right-1,7), self.addij(i,right-2,7)
        time.sleep(1)
        #z = 0
        #for z in range(14):
        #    time.sleep(.1)
        #    left, right = self.move(left,right,i)
        # Implement row flushing animation and matrix shifting here
    def move(self,l,r,i):
        self.delij(i,l), self.delij(i,r)
        l = l+1
        r = r-1
        self.addij(i,l,7),self.addij(i,r,7)
        time.sleep(1)
        return l,r


#########################################################
############# Main code #################################
#########################################################
  
def main(): 
        
        ##### create a window, canvas 
        root = Tk()                # instantiate a tkinter window
        mesh = Grid(root,50,30,20) # instantiate a Grid object
        mesh.random_pixels(25,1) # generate 25 random (white) pixels in the Grid

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:mesh.addxy(e))
        root.bind("<Button-3>",lambda e:mesh.delxy(e))

        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

