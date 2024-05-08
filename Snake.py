from tkinter import *
from Grid import Grid
from Pixel import Pixel
import time, random


### complete class Snake
class Snake(Grid):
    def __init__(self,root,obstacle,fruits,nrow=50,ncol=30,scale=20):
        super().__init__(root,nrow,ncol,scale)
        self.nob = obstacle
        self.random_pixels(self.nob, 1)
        self.nfr = fruits
        self.random_pixels(self.nob, 3)
        
        self.i = self.nrow // 2
        self.j = self.ncol // 2
        
        self.__pause = False
        self.__game_over = False
        
        self.direction = random.choice([[0,1],[0-1],[1,0],[-1,0]])
        
        if self.direction == [0,1]:
            jhead,jbody1,jbody2,jbody3 = self.j,self.j-1,self.j-2,self.j-3
            ihead,ibody1,ibody2,ibody3 = self.i,self.i,self.i,self.i
        elif self.direction == [0,-1]:
            jhead,jbody1,jbody2,jbody3 = self.j,self.j+1,self.j+2,self.j+3
            ihead,ibody1,ibody2,ibody3 = self.i,self.i,self.i,self.i
        elif self.direction == [1,0]:
            jhead,jbody1,jbody2,jbody3 = self.j,self.j,self.j,self.j
            ihead,ibody1,ibody2,ibody3 = self.i,self.i-1,self.i-2,self.i-3
        else:
            jhead,jbody1,jbody2,jbody3 = self.j,self.j,self.j,self.j
            ihead,ibody1,ibody2,ibody3 = self.i,self.i+1,self.i+2,self.i+3
            
        self.head=Pixel(self.canvas,ihead,jhead,self.nrow,self.ncol,self.scale,4,self.direction)
        
        self.snake = [Pixel(self.canvas,ibody3,jbody3,self.nrow,self.ncol,self.scale,5,self.direction),Pixel(self.canvas,ibody2,jbody2,self.nrow,self.ncol,self.scale,5,self.direction),Pixel(self.canvas,ibody1,jbody1,self.nrow,self.ncol,self.scale,5,self.direction),self.head]
    
    def is_pause(self):
        return self.__pause
    
    def pause(self):
        if self.__pause:
            self.__pause = False
        else:
            self.__pause = True
    
    def is_game_over(self):
        return self.__game_over
    
    def next(self):
        
        if self.direction == [1,0]:
            next_i = self.snake[-1].i +1
            next_j = self.snake[-1].j
        elif self.direction == [-1,0]:
            next_i = self.snake[-1].i -1
            next_j = self.snake[-1].j
        elif self.direction == [0,1]:
            next_i = self.snake[-1].i
            next_j = self.snake[-1].j +1
        else:
            next_i = self.snake[-1].i
            next_j = self.snake[-1].j - 1
            
        fruit_left = False
        
        no_head = False
        
        for row in range(self.nrow):
            for col in range(self.ncol):
                
                if self.Integer[row,col] == 1 and next_i == row and next_j == col:
                    self.__game_over = True
                    text= self.canvas.create_text(self.ncol*self.scale//2,self.nrow*self.scale//2,text="GAME OVER",fill="red",font=("Comic Sans", 25, "bold"))
                    no_head = True
                
                if self.Integer[row, col] == 3 and next_i == row and next_j == col:
                    self.del_ij(row, col)
                    
                    if self.direction == [-1,0]:
                        new_i, new_j = self.snake[0].i+1, self.snake[0].j
                    elif self.direction == [1,0]:
                        new_i, new_j = self.snake[0].i-1, self.snake[0].j
                    elif self.direction == [0,1]:
                        new_i, new_j = self.snake[0].i, self.snake[0].j-1
                    else:
                        new_i, new_j = self.snake[0].i, self.snake[0].j+1
                        
                    self.snake.insert(0,Pixel(self.canvas, new_i, new_j, self.nrow, self.ncol,self.scale,5,self.direction))
                
                if self.Integer[row, col] == 3:
                    fruit_left = True
                
        if not fruit_left:
            self.__game_over = True
            text= self.canvas.create_text(self.ncol*self.scale//2,self.nrow*self.scale//2,text="YOU WON",fill="yellow",font=("Comic Sans", 25, "bold"))
        for piece in range(len(self.snake)-1):
            if self.snake[piece].i == next_i and self.snake[piece].j == next_j:
                
                self.__game_over = True
                text= self.canvas.create_text(self.ncol*self.scale//2,self.nrow*self.scale//2,text="GAME OVER",fill="red",font=("Comic Sans", 25, "bold"))
        count = 0
        
        for pixel in range(len(self.snake)-1):
            self.snake.append(Pixel(self.canvas,self.snake[pixel+1].i,self.snake[pixel+1].j,self.nrow,self.ncol,self.scale, 5))
            count += 1
        
        for green in range(len(self.snake)-count):
            self.snake[green].delete()
        for old_pix in range(len(self.snake)-count):
            del self.snake[0]
            
        if self.direction == [-1,0] and not no_head:
            self.head.up()
            self.head.next()
            new_head = Pixel(self.canvas,self.head.i,self.head.j,self.nrow,self.ncol,self.scale,4)
            self.snake.append(new_head)
            self.head.delete()
            self.head = new_head

        if self.direction == [1,0] and not no_head:
            self.head.down()
            self.head.next()
            new_head = Pixel(self.canvas,self.head.i,self.head.j,self.nrow,self.ncol,self.scale,4)
            self.snake.append(new_head)
            self.head.delete()
            self.head = new_head
            
        if self.direction == [0,-1] and not no_head:
            self.head.left()
            self.head.next()
            new_head = Pixel(self.canvas,self.head.i,self.head.j,self.nrow,self.ncol,self.scale,4)
            self.snake.append(new_head)
            self.head.delete()
            self.head = new_head

        if self.direction == [0,1] and not no_head:
            self.head.right()
            self.head.next()
            new_head = Pixel(self.canvas,self.head.i,self.head.j,self.nrow,self.ncol,self.scale,4)
            self.snake.append(new_head)
            self.head.delete()
            self.head = new_head
    
    def up(self):
        if self.direction != [1,0]:
            self.direction = [-1,0]
            self.next()
    
    def down(self):
        if self.direction != [-1,0]:
            self.direction = [1,0]
            self.next()

    def left(self):
        if self.direction != [0,1]:
            self.direction = [0,-1]
            self.next()

    def right(self):
        if self.direction != [0,-1]:
            self.direction = [0,1]
            self.next()


#########################################################
############# Main code #################################
#########################################################
    

  
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        python = Snake(root,20,20) #20 obstacles, and 20 fruits
        #python = Snake(root,5,5,25,25,30) # 5 obstacles/fruits, 25 row, 25 column, 30 scale
        
        
        ####### Tkinter binding mouse actions
        root.bind("<Right>",lambda e:python.right())
        root.bind("<Left>",lambda e:python.left())
        root.bind("<Up>",lambda e:python.up())
        root.bind("<Down>",lambda e:python.down())
        root.bind("<p>",lambda e:python.pause())
       
        while True:
            if not python.is_pause(): python.next()
            root.update()
            time.sleep(0.1)  # wait few second (simulation)
            if python.is_game_over(): break
            
        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

