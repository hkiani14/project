#Name 1: Ankush Achwani, Student ID: 34367855
#Name 2: Huzaifa Kiani, Student ID: 34434370

#importing the libraries
from tkinter import *
from Grid import Grid
from Tetrominoes import Tetrominoes
import numpy as np
import time


# To complete
# defining class tetris which is inherited from class grid
class Tetris(Grid):
    def __init__(self,root, nrow, ncol, scale):
        self.root = root
        self.nrow = nrow
        self.ncol = ncol
        self.scale = scale
        self.blocks = []
        self.block = None
        self.direction = "none"
        self.__paused = False
        self.__gameover = False

        super().__init__(self.root, self.nrow, self.ncol, self.scale) 
    
    #method to handle next step of game
    def next(self):
        if self.block == None:
            # If there's no current falling block, create a new one
            self.block = Tetrominoes(self.canvas, self.nrow, self.ncol, self.scale).random_select(self.canvas, self.nrow, self.ncol, self.scale)
            self.block.activate()
            self.blocks.append(self.block)
            # Check if the new block overlaps with existing blocks, indicating game over
            if self.is_overlapping():
                self.__gameover = True

        # If there's a current falling block, move it according to user input
        else:
            if self.direction == "right" and not self.can_go_right():
                self.block.right()
                self.direction = "none"

            elif self.direction == "left" and not self.can_go_left():
                self.block.left()
                self.direction = "none"

            elif self.direction == "up":
                self.block.rotate()
                self.direction = "none"

            elif self.direction == "down" and not self.is_overlapping():
                self.block.down()
                self.block.down()
                self.direction = "none" 
            else :
                self.block.down()

            self.blocks[len(self.blocks)-1] = self.block


            # Check if the falling block has reached the bottom limit
            if self.is_bottom_limit_reached(self.block.i, self.block.h, self.nrow):
                self.block = None
                return
            
            # Check if the falling block overlaps with existing blocks
            if self.is_overlapping():
                self.block = None
                return

    # Method to handle right arrow key press        
    def right(self):
        self.direction = "right"
    # Method to handle left arrow key press  
    def left(self):
        self.direction = "left"
    # Method to handle up arrow key press  
    def up(self):
        self.direction = "up"
    # Method to handle down arrow key press  
    def down(self):
        self.direction = "down"
    
    # Method to check if the falling block has reached the bottom limit
    def is_bottom_limit_reached(self, i, h, nrow):
        if i < nrow - h:
            return False
        else:
            return True
    # Method to check if the falling block overlaps with existing blocks    
    def is_overlapping(self):
        for index in range(0,len(self.blocks)-1):
            prev_block_coordinates = self.blocks[index].coordinates[-1]
            curr_block_coordinates = self.blocks[-1].coordinates[-1]
            for x,y in prev_block_coordinates:
                for ii,jj in curr_block_coordinates:
                    if x == ii and y == jj+1:
                        return True
        return False
    
     # Method to check if the falling block can move left
    def can_go_left(self):
        for index in range(0,len(self.blocks)-1):
            prev_block_coordinates = self.blocks[index].coordinates[-1]
            curr_block_coordinates = self.blocks[-1].coordinates[-1]
            for x,y in prev_block_coordinates:
                for ii,jj in curr_block_coordinates:
                    if x == ii-1 and y == jj:
                        return True
        return False
    
     # Method to check if the falling block can move right
    def can_go_right(self):
        for index in range(0,len(self.blocks)-1):
            prev_block_coordinates = self.blocks[index].coordinates[-1]
            curr_block_coordinates = self.blocks[-1].coordinates[-1]
            for x,y in prev_block_coordinates:
                for ii,jj in curr_block_coordinates:
                    if x == ii+1 and y == jj:
                        return True
        return False

    # Method to pause
    def pause(self):
        self.__paused = True if self.__paused == False else False

    # Method to check if the game is paused
    def is_pause(self):
        return self.__paused
    
    #Method to check if the game is over
    def is_game_over(self):
        return self.__gameover
    
    #Method to display game over message
    def game_over(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2,
                    font=('consolas',20), text="GAME OVER", fill="red", tag="gameover")
    
    # Method to flush completed rows
    def flush_row(self):
        for row in range(self.nrow-1,-1,-1):
            pass

    # Method to check if rows can be flushed
    def can_flush(self):
        pass
    

#Defining the main function
def main():
    nrow=24
    ncol=24
    scale=20
    root = Tk() 

    game=Tetris(root,nrow,ncol,scale) 
    
    root.bind("<Up>",lambda e:game.up())
    root.bind("<Left>",lambda e:game.left())
    root.bind("<Right>",lambda e:game.right())
    root.bind("<Down>",lambda e:game.down())
    root.bind("<p>",lambda e:game.pause())        

    while True:
        if not game.is_pause(): 
            game.next()
        root.update()   # update the graphic
        time.sleep(0.25)  # wait few second (simulation)
        if game.is_game_over():
            game.game_over()
            break
    
    root.mainloop() # wait until the window is closed     

if __name__=="__main__":
    main()

