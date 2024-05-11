# Import necessary libraries
from tkinter import *
from Pixel import Pixel  
import numpy as np
import random, time

# To complete
class Grid():
    # Constructor method
    def __init__(self, root, nrow, ncol, scale):
        self.root = root
        self.canvas = Canvas(root, width=nrow*scale, height=ncol*scale)
        self.canvas.pack()
        self.nrow = nrow
        self.ncol = ncol
        self.scale = scale
        self.pixels = []
        self.matrix = np.zeros((nrow, ncol), dtype=int)

        # Draw grid lines on canvas
        self.canvas.create_rectangle(0, 0, nrow*scale, ncol*scale, fill="black")  # Draw the gray grid background
        for i in range(ncol+1):
            x1 = 0
            y1 = i * scale
            x2 = nrow * scale
            y2 = i * scale
            self.canvas.create_line(x1, y1, x2, y2, fill="gray")
        for i in range(nrow+1):
            x1 = i * scale
            y1 = 0
            x2 = i * scale
            y2 = ncol * scale
            self.canvas.create_line(x1, y1, x2, y2, fill="gray")

    # Method to add a pixel at given indices with specified color
    def addij(self, i, j, c):
        x = i * self.scale
        y = j * self.scale
        pix = Pixel(self.canvas, i, j, self.nrow, self.ncol, self.scale, c)
        self.pixels.append(pix)
        self.matrix[i, j] = c

    # Method to generate random pixels with specified color
    def random_pixels(self, num_pixels, c):
        for _ in range(num_pixels):
            i = random.randint(0, self.nrow-1)
            j = random.randint(0, self.ncol-1)
            while self.matrix[i, j] != 0:
                i = random.randint(0, self.nrow-1)
                j = random.randint(0, self.ncol-1)
            self.addij(i, j, c)

    # Method to add a pixel at given coordinates
    def addxy(self, x, y):
        i = x // self.scale
        j = y // self.scale
        if i >= 0 and i < self.nrow and j >= 0 and j < self.ncol:
            if self.matrix[i, j] == 0:
                c = 1  # Default color (white)
                self.addij(i, j, c)
                info = f"insert {x} {y} {j} {i} 0"
                print(info)
            else:
                info = f"insert {x} {y} {j} {i} {self.matrix[i, j]}"
                print(info)

    # Method to delete a pixel at given indices
    def delij(self, i, j):
        c = self.matrix[i, j]
        if c != 0:
            self.matrix[i, j] = 0
            self.reset()

    # Method to delete a pixel at given coordinates
    def delxy(self, x, y):
        i = x // self.scale
        j = y // self.scale
        if i >= 0 and i < self.nrow and j >= 0 and j < self.ncol:
            if self.matrix[i, j] != 0:
                info = f"delete {x} {y} {j} {i} {self.matrix[i, j]}"
                print(info)
                self.delij(i, j)
            else:
                print("NANANANANAN", y)
                self.flush_row(j)

    # Method to flush a row by shifting elements and animating the process
    def flush_row(self, j):
        # Create big purple pixels
        pix_left = [Pixel(self.canvas, i, j, self.nrow, self.ncol, self.scale, 7, vector=[0, 1]) for i in range(3)]
        pix_right = [Pixel(self.canvas, i, j, self.nrow, self.ncol, self.scale, 7, vector=[0, -1]) for i in range(3)]
        big_pix = pix_left + pix_right

        # Animate the big purple pixels
        i = 0
        while i < self.ncol // 2:
            for p in big_pix:
                p.next()
                self.canvas.move(p.rectangle, p.vector[1] * p.scale, p.vector[0] * p.scale)
            i += 1
            self.canvas.update()
            time.sleep(0.02)

        # Delete the big purple pixels
        for p in big_pix:
            p.delete()

        # Shift the matrix
        self.matrix[:, j] = self.matrix[:, j - 1]
        self.matrix[:, j - 1] = self.matrix[:, j - 2]
        self.matrix[:, j - 2] = np.zeros(self.nrow)

        # Reset the canvas with the new grid configuration
        self.reset()

    # Method to reset canvas with current grid configuration
    def reset(self):
        for pixel in self.pixels:
            pixel.delete()
        self.pixels = []
        for i in range(self.nrow):
            for j in range(self.ncol):
                if self.matrix[i, j] != 0:
                    self.addij(i, j, self.matrix[i, j])

# Main function
def main(): 
    # Create a window and instantiate a Grid object
    root = Tk()                
    mesh = Grid(root, 30, 50, 20)  # 30 rows, 50 columns, scale of 20

    # Generate 25 random (white) pixels in the Grid
    mesh.random_pixels(25, 1)

    # Bind mouse actions to Grid methods
    root.bind("<Button-1>", lambda e: mesh.addxy(e.x, e.y))  # Left click to add pixel
    root.bind("<Button-2>", lambda e: mesh.delxy(e.x, e.y))  # Middle click to delete pixel
    root.bind("<Button-3>", lambda e: mesh.delxy(e.x, e.y))  # Right click to delete pixel

    root.mainloop()  # Wait until the window is closed

# Entry point of the program
if __name__ == "__main__":
    main()
