from tkinter import*
from PIL import ImageGrab

class ControlInterface():
  def __init__(self,tK_object,window,sprite):
    self.robot = sprite
    self.window = window
    self.tK_object = tK_object
    self.build_buttons()

  def build_buttons(self):
    button = Button(self.window, text = 'Forward', command = self.robot.Forward, bg = "red")
    button.grid(row = 1, column = 2, pady=20, padx = 20)

    button = Button(self.window, text = 'Backward', command = self.robot.Backward, bg = "green")
    button.grid(row = 2, column = 2, pady=20, padx = 20)

    button = Button(self.window, text = 'Left', command = self.robot.Left, bg = "yellow")
    button.grid(row = 2, column = 1, pady=20, padx = 20)

    button = Button(self.window, text = 'Right', command = self.robot.Right, bg = "white")
    button.grid(row = 2, column = 3,pady=20, padx = 20)

    button = Button(self.window, text = 'Take Picture', command = self.take_picture, bg = "orange")
    button.grid(row = 3, column = 2,pady=20, padx = 20)

  def take_picture(self):
    print('taking picture!')
    x0 = self.tK_object.winfo_rootx()
    y0 = self.tK_object.winfo_rooty()
    x1 = x0 + self.tK_object.winfo_width()
    y1 = y0 + self.tK_object.winfo_height()
    ImageGrab.grab().crop((x0, y0, x1, y1)).save("TurtleArt.png")