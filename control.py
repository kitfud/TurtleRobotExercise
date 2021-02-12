from tkinter import*


class ControlInterface():
  def __init__(self,window,sprite):
    self.robot = sprite
    self.window = window

    button = Button(self.window, text = 'Forward', command = self.robot.Forward, bg = "red")
    button.grid(row = 1, column = 2, pady=20, padx = 20)

    button = Button(self.window, text = 'Backward', command = self.robot.Backward, bg = "green")
    button.grid(row = 2, column = 2, pady=20, padx = 20)

    button = Button(self.window, text = 'Left', command = self.robot.Left, bg = "yellow")
    button.grid(row = 2, column = 1, pady=20, padx = 20)

    button = Button(self.window, text = 'Right', command = self.robot.Right, bg = "white")
    button.grid(row = 2, column = 3,pady=20, padx = 20)