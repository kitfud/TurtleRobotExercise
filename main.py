import turtle
from tkinter import*

class TurtleRobot():
  def __init__(self,name,color):
    self.name = name
    self.sprite = turtle.Pen()
    self.sprite.color(color)

  def Forward(self): #function        
    print (self.name + ' is running forward')
    self.sprite.forward(100)

  def Backward(self):
    print (self.name + ' is running backward')
    self.sprite.backward(100)

  def Right(self):
    print (self.name + ' is going right')
    self.sprite.right(20)

  def Left(self):
    print (self.name + ' is going left')
    self.sprite.left(20)

bob = TurtleRobot("bob","red")



# window = Tk()                             #main window

# button = Button(window, text = 'Forward', command = Forward, bg = "red")
# button.grid(row = 1, column = 2, pady=20, padx = 20)

# button = Button(window, text = 'Backward', command = Backward, bg = "green")
# button.grid(row = 2, column = 2, pady=20, padx = 20)

# button = Button(window, text = 'Left', command = Left, bg = "yellow")
# button.grid(row = 2, column = 1, pady=20, padx = 20)

# button = Button(window, text = 'Right', command = Right, bg = "white")
# button.grid(row = 2, column = 3,pady=20, padx = 20)


# window.mainloop()