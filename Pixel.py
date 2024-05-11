#Name 1: Ankush Achwani, Student ID: 34367855
#Name 2: Huzaifa Kiani, Student ID: 34434370

# Importing necessary libraries
from tkinter import *
import time
import random


# To complete
# Class definition for a pixel
class Pixel:
    # List of available colors
    color=['black','white','yellow','red','blue','green','orange','purple','brown','cyan']
    
    # Constructor method
    def __init__(self, canvas, i, j, nrow, ncol, scale, c, vector=[0,0]):
        self.canvas=canvas
        self.i=i%nrow  # Ensure periodic boundary conditions
        self.j=j%ncol  # Ensure periodic boundary conditions
        self.nrow=nrow
        self.ncol=ncol
        self.scale=scale
        self.c=c
        self.vector=vector
        
        # Create a rectangle representing the pixel on the canvas
        self.rectangle= self.canvas.create_rectangle(
            self.i*self.scale,
            self.j*self.scale,
            (self.i + 1) * self.scale,
            (self.j + 1) * self.scale,
            fill=self.color[self.c]  # Fill with specified color
        )

    # String representation of the pixel
    def __str__(self):
        return f"({self.i},{self.j}) {self.color[self.c]}"
    
    # Movement methods
    def right(self):
        self.vector=[0,1]
    def left(self):
        self.vector=[0,-1]
    def up(self):
        self.vector=[-1,0]
    def down(self):
        self.vector=[1,0]

    # Method to move the pixel to the next position
    def next(self):
        delta_i = self.vector[1]
        delta_j = self.vector[0]

        # Compute new indices considering periodic boundary conditions
        new_i = (self.i + delta_i) % self.nrow
        new_j = (self.j + delta_j) % self.ncol

        # Wrap around if indices go out of bounds
        if new_i < 0:
            new_i = self.nrow - 1
        if new_j < 0:
            new_j = self.ncol - 1

        # Compute displacement
        x_displacement = (new_i - self.i) * self.scale
        y_displacement = (new_j - self.j) * self.scale

        # Move the pixel on the canvas
        self.canvas.move(self.rectangle, x_displacement, y_displacement)
        self.i = new_i
        self.j = new_j

    # Method to delete the pixel from the canvas
    def delete(self):
        self.canvas.delete(self.rectangle)
     
#################################################################
########## TESTING FUNCTIONS ###################################
#################################################################

# Function to delete all elements from the canvas
def delete_all(canvas):
    canvas.delete("all")
    print("Delete All")

# Function to test generating 10 points at random
def test1(canvas, nrow, ncol, scale):
    print("Generate 10 points at random")
    random.seed(4)  # Set seed for reproducibility
    for k in range(10):
        i=random.randint(0,nrow-1) 
        j=random.randint(0,ncol-1)
        c=random.randint(1,9)    # Choose random color
        pix=Pixel(canvas, i, j, nrow, ncol, scale, c)
        print(pix)

# Function to test generating 10 points at random using modulo
def test2(canvas, nrow, ncol, scale):
    print("Generate 10 points at random (using modulo)")
    random.seed(5)  # Set seed for reproducibility
    for k in range(10):
        i=random.randint(0,nrow-1)*34
        j=random.randint(0,ncol-1)*13
        ij=str(i)+","+str(j)
        c=random.randint(1,9)    # Choose random color
        pix=Pixel(canvas, i, j, nrow, ncol, scale, c)
        print(ij,"->",pix)

# Function to test moving one point along a square path
def test3(root, canvas, nrow, ncol, scale):
    print("Move one point along a square")

    pix=Pixel(canvas, 35, 35, nrow, ncol, scale, 3)  # Create a pixel at specified position and color
    pix.vector=[-1,0]  # Set initial direction (up)
    for i in range(30):
        pix.next()       # Move the pixel
        root.update()    # Update the graphic
        time.sleep(0.05) # Wait for simulation

    # Change direction and repeat for other sides of the square
    pix.vector=[0,-1]  
    for i in range(30):
        pix.next()       
        root.update()    
        time.sleep(0.05) 
    pix.vector=[1,0]   
    for i in range(30):
        pix.next()       
        root.update()    
        time.sleep(0.05)   
    pix.vector=[0,1]    
    for i in range(30):
        pix.next()       
        root.update()    
        time.sleep(0.05)
    # Delete the point after completing the square
    pix.delete()

# Function to test moving four points along a square path
def test4(root, canvas, nrow, ncol, scale):
    print("Move four points along a square")

    pixs=[]  # List to hold pixels
    # Create pixels at specified positions and colors, with initial directions
    pixs.append(Pixel(canvas, 35, 35, nrow, ncol, scale, 3, [-1,0]))
    pixs.append(Pixel(canvas, 35, 5, nrow, ncol, scale, 4, [0,-1]))
    pixs.append(Pixel(canvas, 5, 5, nrow, ncol, scale, 5, [1,0]))
    pixs.append(Pixel(canvas, 5, 35, nrow, ncol, scale, 6, [0,1]))
    
    print("Starting coords")
    for p in pixs: print(p)

    # Move all pixels simultaneously
    for i in range(30):
        for p in pixs:
            p.next()       # Move each pixel
        root.update()      # Update the graphic
        time.sleep(0.05)   # Wait for simulation

    print("Ending coords")
    for p in pixs:
        print(p)
        p.delete()  # Delete each pixel after completing the square path

# Function to test moving one point in any direction using arrow commands
def test5(root, canvas, nrow, ncol, scale):
    print("Move one point any direction -use arrow commands")
    pix=Pixel(canvas, 20, 17, nrow, ncol, scale, 2)  # Create a pixel at specified position and color
    # Bind arrow keys to movement functions
    root.bind("<Right>", lambda e: pix.right())
    root.bind("<Left>", lambda e: pix.left())
    root.bind("<Up>", lambda e: pix.up())
    root.bind("<Down>", lambda e: pix.down())

    # Continuous simulation
    while True:
        pix.next()        # Move the pixel
        root.update()     # Update the graphic
        time.sleep(0.05)  # Wait for simulation

###################################################
#################### Main method ##################
###################################################

# Main function
def main():
    ##### Create a window, canvas
    root = Tk()  # Instantiate a tkinter window
    nrow=40
    ncol=40
    scale=20
    canvas = Canvas(root, width=ncol*scale, height=nrow*scale, bg="black")  # Create a canvas
    canvas.pack()

    # General binding events to choose a testing function
    root.bind("1", lambda e: test1(canvas, nrow, ncol, scale))
    root.bind("2", lambda e: test2(canvas, nrow, ncol, scale))
    root.bind("3", lambda e: test3(root, canvas, nrow, ncol, scale))
    root.bind("4", lambda e: test4(root, canvas, nrow, ncol, scale))
    root.bind("5", lambda e: test5(root, canvas, nrow, ncol, scale))
    root.bind("<d>", lambda e: delete_all(canvas))  # Delete all elements on canvas with 'd' key
    
    root.mainloop()  # Wait until the window is closed
        
if __name__=="__main__":
    main()