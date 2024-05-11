#Name 1: Ankush Achwani, Student ID: 34367855
#Name 2: Huzaifa Kiani, Student ID: 34434370


from tkinter import *
from Pixel import Pixel
import time, random
import numpy as np



class Tetrominoes:

    ## to complete
    # Define the color options for tetrominoes
    color=['black','white','yellow','red','blue','green','orange','purple','brown','cyan']
    # Constructor method
    def __init__(self, canvas, nrow, ncol, scale, c=2, patterns=None):
        self.canvas = canvas
        self.nrow = nrow
        self.ncol = ncol
        self.scale = scale
        self.c = c
        self.patterns = patterns if patterns else [np.array([[2,2,2],[2,0,2],[2,2,2]])]
        self.nbpattern = len(self.patterns)
        self.current = 0
        self.name = "Basic"
        self.h, self.w = self.patterns[self.current].shape
        self.i = 0
        self.j = 0
        self.pixels = []
        self.coordinates = []

    # Method to activate a tetromino
    def activate(self, i=0, j=None):
        if j is None:
            j = random.randint(0, self.ncol - self.w)
        self.i = i
        self.j = j
        self.pixels = []
        pattern = self.patterns[self.current]
        templist = []
        for row in range(self.h):
            for col in range(self.w):
                if pattern[row, col] != 0:
                    x = self.j + col
                    y = self.i + row
                    pixel = self.canvas.create_rectangle(
                        x * self.scale,
                        y * self.scale,
                        (x + 1) * self.scale,
                        (y + 1) * self.scale,
                        fill=self.color[pattern[row,col]]
                    )
                    templist.append((x,y))
                    self.pixels.append(pixel)
        self.coordinates.append(templist)

    # Method to get the current pattern
    def get_pattern(self):
        return self.patterns[self.current]

    # Method to rotate a tetromino
    def rotate(self):
        self.delete()
        self.current = (self.current + 1) % self.nbpattern
        self.h, self.w = self.patterns[self.current].shape
        self.activate(self.i, self.j)

    # Method to delete a tetromino
    def delete(self):
        for pixel in self.pixels:
            self.canvas.delete(pixel)

    # Method to move that tetromino left
    def left(self):
        self.delete()
        if self.j > 0:
            self.j -= 1
        self.activate(self.i, self.j)

    # Method to move that tetromino right
    def right(self):
        self.delete()
        if self.j < self.ncol - self.w:
            self.j += 1
        self.activate(self.i, self.j)

    # Method to move that tetromino up
    def up(self):
        self.delete()
        if self.i > 0:
            self.i -= 1
        self.activate(self.i, self.j)

    # Method to move that tetromino down
    def down(self):
        self.delete()
        if self.i < self.nrow - self.h:
            self.i += 1
        self.activate(self.i, self.j)

    # Method to randomly select a tetromino shape
    @staticmethod
    def random_select(canv,nrow,ncol,scale):
        t1=TShape(canv,nrow,ncol,scale)
        t2=TripodA(canv,nrow,ncol,scale)
        t3=TripodB(canv,nrow,ncol,scale)
        t4=SnakeA(canv,nrow,ncol,scale)
        t5=SnakeB(canv,nrow,ncol,scale)
        t6=Cube(canv,nrow,ncol,scale)
        t7=Pencil(canv,nrow,ncol,scale)        
        return random.choice([t1,t2,t3,t4,t5,t6,t7,t7]) #a bit more change to obtain a pencil shape

#########################################################
############# All Child Classes #########################
#########################################################

# Define each tetromino shape
class TShape(Tetrominoes):
    def __init__(self, canvas, nrow, ncol, scale):
        patterns = [
            np.array([[0,3,0],[0,3,0],[3,3,3]]),
            np.array([[3,0,0],[3,3,3],[3,0,0]]),
            np.array([[3,3,3],[0,3,0],[0,3,0]]),
            np.array([[0,0,3],[3,3,3],[0,0,3]])
        ]
        super().__init__(canvas,nrow,ncol,scale,1, patterns)
        self.name = "TShape"

class TripodA(Tetrominoes):
    def __init__(self,canvas,nrow,ncol,scale):
        patterns = [
            np.array([[0,4,0],[0,4,0],[4,0,4]]),
            np.array([[4,0,0],[0,4,4],[4,0,0]]),
            np.array([[4,0,4],[0,4,0],[0,4,0]]),
            np.array([[0,0,4],[4,4,0],[0,0,4]])
        ]
        super().__init__(canvas,nrow,ncol,scale,1,patterns)
        self.name="TripodA"

class TripodB(Tetrominoes):
    def __init__(self,canvas,nrow,ncol,scale):
        patterns = [
            np.array([[0,5,0],[5,0,5],[5,0,5]]),
            np.array([[5,5,0],[0,0,5],[5,5,0]]),
            np.array([[5,0,5],[5,0,5],[0,5,0]]),
            np.array([[0,5,5],[5,0,0],[0,5,5]])
        ]
        super().__init__(canvas,nrow,ncol,scale,1,patterns)
        self.name="TripodB"

class SnakeA(Tetrominoes):
    def __init__(self,canvas,nrow,ncol,scale):
        patterns = [
            np.array([[6,6,0],[0,6,0],[0,6,6]]),
            np.array([[0,0,6],[6,6,6],[6,0,0]])  
        ]
        super().__init__(canvas,nrow,ncol,scale,1,patterns)
        self.name="SnakeA"

class SnakeB(Tetrominoes):
    def __init__(self,canvas,nrow,ncol,scale):
        patterns = [
            np.array([[0,7,7],[0,7,0],[7,7,0]]),
            np.array([[7,0,0],[7,7,7],[0,0,7]])
        ]
        super().__init__(canvas,nrow,ncol,scale,1,patterns)
        self.name="SnakeB"

class Cube(Tetrominoes):
    def __init__(self,canvas,nrow,ncol,scale):
        patterns = [
            np.array([[8,8,8],[8,8,8],[8,8,8]]),
            np.array([[0,8,0],[8,8,8],[0,8,0]]),
            np.array([[8,0,8],[0,8,0],[8,0,8]])
        ]
        super().__init__(canvas,nrow,ncol,scale,1,patterns)
        self.name="Cube"

class Pencil(Tetrominoes):
    def __init__(self,canvas,nrow,ncol,scale):
        patterns = [
            np.array([[9,0,0],[9,0,0],[9,0,0]]),
            np.array([[0,0,0],[0,0,0],[9,9,9]]),
            np.array([[0,0,9],[0,0,9],[0,0,9]]),
            np.array([[0,0,0],[0,0,0],[9,9,9]])
        ]
        super().__init__(canvas,nrow,ncol,scale,1,patterns)
        self.name="Pencil"

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
    print("  current pattern:\n",tetro1.get_pattern()) # retrieve current pattern
    print("  height/width:",tetro1.h,tetro1.w)
    tetro1.activate(nrow//2,ncol//2)        # activate and put in the middle
    print("  i/j coords:  ",tetro1.i,tetro1.j)

    pattern=np.array([[0,3,0],[3,3,3],[0,3,0],[3,0,3],[3,0,3]]) # matrix motif
    tetro2=Tetrominoes(canvas,nrow,ncol,scale,3,[pattern]) # instantiate (list of patterns-- 1 item here)
    print("\nTetro2",tetro2.name)
    print("  number of patterns:",tetro2.nbpattern)
    print("  current pattern:\n",tetro2.get_pattern()) # retrieve current pattern
    print("  height/width:",tetro2.h,tetro2.w)
    tetro2.activate()        # activate and place at random at the top
    print("  i/j coords:  ",tetro2.i,tetro2.j)

    
    
def test2(root,canvas,nrow,ncol,scale):
    print("Generate a 'square' Tetromino (with double shape) and rotate")
    
    print("My Tetro")
    pattern1=np.array([[4,0,0],[0,4,0],[0,0,4]]) # matrix motif
    pattern2=np.array([[0,0,4],[0,4,0],[4,0,0]]) # matrix motif
    tetro=Tetrominoes(canvas,nrow,ncol,scale,4,[pattern1,pattern2]) # instantiate (list of patterns-- 2 items here)
    print("  number of patterns:",tetro.nbpattern)
    print("  height/width:",tetro.h,tetro.w)
    tetro.activate(nrow//2,ncol//2)        # activate and place in the middle
    print("  i/j coords:  ",tetro.i,tetro.j)

    for k in range(10): # make 10 rotations
        tetro.rotate() # rotate (change pattern)
        print("  current pattern:\n",tetro.get_pattern()) # retrieve current pattern
        root.update()
        time.sleep(0.5)
    tetro.delete() # delete tetro (delete every pixels)


def rotate_all(tetros): #auxiliary routine
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
    t7=Pencil(canvas,nrow,ncol,scale)
    tetros=[t0,t1,t2,t3,t4,t5,t6,t7]

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

