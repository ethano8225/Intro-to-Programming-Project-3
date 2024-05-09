from tkinter import *
from Pixel import Pixel
import numpy as np
import random, time


class Grid:
    def __init__(self,root,nrow,ncol,scale):
        self.root=root
        self.nrow=nrow
        self.ncol=ncol          #set default values
        self.scale=scale
        self.canvas=Canvas(root,width=ncol*scale,height=nrow*scale, bg='white')
        self.canvas.pack()
        self.Integer= np.zeros((self.nrow,self.ncol),dtype=np.int8)
        self.pixelist=[]
        for row in range(nrow):
            for col in range(ncol):     
                self.pixelist.append(Pixel(self.canvas,row,col,self.nrow,self.ncol,self.scale,0))
        
    def random_pixels(self,num,color_id):
        for k in range(num):
            i = random.randint(0,self.nrow-1)
            j=random.randint(0,self.ncol-1)     #add random pixels to the screen using random (imported)
            self.add_ij(i,j,color_id)

    def addxy(self,x,y):
        print(f"insert {x} {y} {y//self.scale} {x//self.scale} {self.Integer[y//self.scale,x//self.scale]}")
        self.add_ij(y//self.scale,x//self.scale,1)      #adds the point to the graph

    def add_ij(self,i,j,c):
        if c>0:                 #actually adds the point here
            self.pixelist.append(Pixel(self.canvas,i,j,self.nrow,self.ncol,self.scale,c))
            self.Integer[i,j] = c

    def delxy(self,x,y):            #delete the point from x,y
        print(f"delete {x} {y} {y//self.scale} {x//self.scale} {self.Integer[y//self.scale,x//self.scale]}")
        self.del_ij(y//self.scale,x//self.scale)

    def del_ij(self,i,j):
        if self.Integer[i,j] != 0:      #actually make the change on grid
            self.Integer[i,j] = 0
            self.reset()
        else:
            self.flush(i,j)

    def reset(self):
        for pixel in self.pixelist:
                pixel.delete()
        for row in range(self.nrow):
            for col in range(self.ncol):        #reset the grid,
                if self.Integer[row, col] > 0:
                    self.add_ij(row,col,self.Integer[row,col])
                else:
                    self.pixelist.append(Pixel(self.canvas,row,col,self.nrow,self.ncol,self.scale,0))
                                
        
        
    def flush(self,i,j=0):
                pixels = []
                pixels.append(Pixel(self.canvas,i,0,self.nrow,self.ncol,self.scale,7,[0,1]))
                pixels.append(Pixel(self.canvas,i,1,self.nrow,self.ncol,self.scale,7,[0,1]))
                pixels.append(Pixel(self.canvas,i,2,self.nrow,self.ncol,self.scale,7,[0,1]))
                    #adds the points to the left and right
                pixels.append(Pixel(self.canvas,i,self.ncol,self.nrow,self.ncol,self.scale,7,[0,-1]))
                pixels.append(Pixel(self.canvas,i,self.ncol-1,self.nrow,self.ncol,self.scale,7,[0,-1]))
                pixels.append(Pixel(self.canvas,i,self.ncol-2,self.nrow,self.ncol,self.scale,7,[0,-1]))
                
                for rowflush in range(self.ncol):
                        for p in pixels:
                                p.next()        #this moves the purple lines for animation
                        self.root.update()
                        time.sleep(0.01)
                self.Integer[1:i+1,:]=self.Integer[0:i,:]
                self.Integer[0,:] = 0
                self.reset()            #resets the row

#########################################################
############# Main code #################################
#########################################################
  
def main(): 
        
        ##### create a window, canvas 
        root = Tk()                # instantiate a tkinter window
        mesh = Grid(root,50,30,20) # instantiate a Grid object
        mesh.random_pixels(25,1) # generate 25 random (white) pixels in the Grid

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>", lambda e: mesh.addxy(e.x, e.y))
        root.bind("<Button-3>", lambda e: mesh.delxy(e.x, e.y))

        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()