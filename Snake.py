#Name 1: Ankush Achwani, Student ID: 34367855
#Name 2: Huzaifa Kiani, Student ID: 34434370

# Importing the libraries
from tkinter import *
from Grid import Grid
from Pixel import Pixel
import time

# To complete
# Creating class snake that's inherited from class grid
class Snake(Grid):

    # Define colors for different elements of the game
    color=['black','white','yellow','red','blue','green','orange','purple','brown','cyan']
    #Constructor function
    def __init__(self, root, nrow, ncol, scale, snake_bodies = [[17,20,5],[18,20,5],[19,20,5],[20,20,4]]):
        self.root = root
        self.nrow = nrow
        self.ncol = ncol
        self.scale = scale
        self.snake_bodies = snake_bodies
        self.direction = -1  # Initial direction (right)
        self.snake_pixels = []  # List to store snake's body pixels
        self.__gameover = False  # Flag to indicate if the game is over
        self.__number_of_fruits = 20  # Number of fruits
        self.__paused = False  # Flag to indicate if the game is paused

        # Call the constructor of the Grid class
        super().__init__(self.root, self.nrow, self.ncol, self.scale) 

        # Create snake's body pixels
        for item in snake_bodies:
            pixel = self.canvas.create_rectangle(item[0]*self.scale, item[1]*self.scale, 
                                                 (item[0]+1)*self.scale, (item[1]+1)*self.scale, 
                                                 fill=self.color[item[2]])
            self.snake_pixels.append(pixel)
     
     # Method to handle right arrow key press       
    def right(self):
        if self.direction!=-3 and self.direction!=-1:
            self.direction = -1
    # Method to handle left arrow key press
    def left(self):
        if self.direction!=-1 and self.direction!=-3:
            self.direction = -3
    # Method to handle up arrow key press
    def up(self):
        if self.direction!=-4 and self.direction!=-2:
            self.direction = -2
    # Method to handle down arrow key press
    def down(self):
        if self.direction!=-2 and self.direction!=-4:
            self.direction = -4

    #Method to define the next function
    def next(self):
        x,y,c = self.snake_bodies[-1]# Get coordinates of snake's head

        # Get coordinates of snake's head
        if self.direction == -2:
            y -= 1
        elif self.direction == -4:
            y += 1
        elif self.direction == -3:
            x -= 1
        elif self.direction == -1:
            x += 1

        # Ensure snake wraps around the grid
        x = x % self.nrow
        y = y % self.ncol
        if x < 0:
            x = self.nrow - 1
        if y < 0:
            y = self.ncol - 1
        
        # Append new head coordinates to snake_bodies
        self.snake_bodies.append([x,y,4])

        head_x , head_y = x, y
        x = x * self.scale
        y = y * self.scale

         #Check for collision with itself
        if self.collision(head_x,head_y):
            self.__gameover = True

        # Check for collision with food
        elif self.food(head_x,head_y):
            square = self.canvas.create_rectangle(x,y,x+self.scale,y+self.scale,fill=self.color[c])
            self.snake_pixels.append(square)
            self.canvas.itemconfig(self.snake_pixels[-2],fill=self.color[5])

        else:
            square = self.canvas.create_rectangle(x,y,x+self.scale,y+self.scale,fill=self.color[c])
            self.snake_pixels.append(square)
            self.canvas.itemconfig(self.snake_pixels[-2],fill=self.color[5])
            del self.snake_bodies[0]
            self.canvas.delete(self.snake_pixels[0])
            del self.snake_pixels[0]
        
    # Method to handle collision with food
    def food(self,x,y):
        current_color = self.matrix[x][y]
        # print("Color at coordinate ({}, {}): {}".format(x, y, current_color))
        if 3 == current_color:
            self.delxy(x*self.scale, y*self.scale)
            self.__number_of_fruits -= 1
            return True
        return False
    
    # Method to check for collisions itself
    def collision(self,x,y):
        if self.__number_of_fruits == 0 :
            return True
        current_color = self.matrix[x,y]
        # print(current_color)
        if 1 == current_color:
            return True
        return False
    
    # Method to check if the game is over
    def is_game_over(self):
        return self.__gameover
    
     # Method to display "Game Over" or "You Won" message
    def game_over(self):
        self.canvas.delete(ALL)
        if self.__number_of_fruits == 0 :
            self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2,
                       font=('consolas',70), text="YOU WON", fill="red", tag="youwon")
        else:
            self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
    
    # Method to pause the game
    def pause(self):
        self.__paused = True if self.__paused == False else False

    # Method to check if the game is paused
    def is_pause(self):
        return self.__paused
    
#########################################################
############# Main code #################################
#########################################################


# Defining the main function    
def main(): 
    nrow=40
    ncol=40
    scale=20
    root = Tk() 
    initial_snake_bodies = [[17,20,5],[18,20,5],[19,20,5],[20,20,4]] # x,y coordinates & color
    snake = Snake(root, nrow, ncol, scale, initial_snake_bodies) 
    snake.random_pixels(20,1)
    snake.random_pixels(20,3)

    root.bind("<Right>",lambda e:snake.right())
    root.bind("<Left>",lambda e:snake.left())
    root.bind("<Up>",lambda e:snake.up())
    root.bind("<Down>",lambda e:snake.down())
    root.bind("<p>",lambda e:snake.pause())
    
    while True:
        if not snake.is_pause(): snake.next()
        root.update()
        time.sleep(0.15)
        if snake.is_game_over():
            snake.game_over()
            break
    root.mainloop()
        

if __name__=="__main__":
    main()

