from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.canvas = Canvas(self, height=200, width = 300)
        self.canvas.grid(row = 0, column = 0, rowspan = 3)

        self.button_up = Button(self, text='UP', command=self.up)
        self.button_up.grid(row = 0, column = 1, columnspan = 2)

        self.button_left = Button(self, text='LEFT', command=self.left)
        self.button_left.grid(row = 1, column = 1)

        self.button_right = Button(self, text='RIGHT', command=self.right)
        self.button_right.grid(row = 1, column = 2)

        self.button_down = Button(self, text='DOWN', command=self.down)
        self.button_down.grid(row = 2, column = 1, columnspan = 2)

        #start the 'pen' in the center of the screen
        self.x, self.y = 150, 100

        self.ent1=Entry(self,width=65)
        self.ent1.grid(row=3,colum=0)
        
        self.button_run=Button(self,text="RUN",command=self.draw)
        self.button_run.grid(row=3,colum=0)
        
    def up(self):
        self.canvas.create_line(self.x, self.y, self.x, self.y - 20)
        self.y -= 20
        
    def down(self):
        self.canvas.create_line(self.x, self.y, self.x, self.y + 20)
        self.y += 20

    def left(self):
        self.canvas.create_line(self.x, self.y, self.x - 20, self.y)
        self.x -= 20
        
    def right(self):
        self.canvas.create_line(self.x, self.y, self.x + 20, self.y)
        self.x += 20
    def draw(self):
        for item in str(self.ent1).get():
            if item=="U":
                self.up
            elif item=="D":
                self.down
            elif item=="L":
                self.left
            elif item=="R":
                self.right
        
            

# main
root = Tk()
root.title("Draw With Buttons!")
root.geometry("500x210")

app = Application(root)
root.mainloop()
