from tkinter import*
from PIL import ImageGrab

class ControlInterface():
  def __init__(self,tK_object,window,sprite):
    self.robot = sprite
    self.window = window
    self.tK_object = tK_object
    self.build_buttons()
    self.forward_pressed = False
    self.backward_pressed = False
    self.left_pressed = False
    self.right_pressed = False

  def build_buttons(self):
    button = Button(self.window, text = 'Forward', bg = "red")
    button.grid(row = 1, column = 2, pady=20, padx = 20)
    button.bind("<ButtonPress>", self.callbackForward)
    button.bind("<ButtonRelease>", self.callbackForward)

    button2 = Button(self.window, text = 'Backward', bg = "green")
    button2.grid(row = 2, column = 2, pady=20, padx = 20)
    button2.bind("<ButtonPress>", self.callbackBackward)
    button2.bind("<ButtonRelease>", self.callbackBackward)

    button3 = Button(self.window, text = 'Left',  bg = "yellow")
    button3.grid(row = 2, column = 1, pady=20, padx = 20)
    button3.bind("<ButtonPress>", self.callbackLeft)
    button3.bind("<ButtonRelease>", self.callbackLeft)

    button4 = Button(self.window, text = 'Right', bg = "white")
    button4.grid(row = 2, column = 3,pady=20, padx = 20)
    button4.bind("<ButtonPress>", self.callbackRight)
    button4.bind("<ButtonRelease>", self.callbackRight)

    button5 = Button(self.window, text = 'Take Picture', command = self.take_picture, bg = "orange")
    button5.grid(row = 3, column = 2,pady=20, padx = 20)
  
  def callbackForward(self,event):
    self.forward_pressed = not self.forward_pressed
   

  def callbackBackward(self,event):
    self.backward_pressed = not self.backward_pressed
    

  def callbackLeft(self,event):
    self.left_pressed = not self.left_pressed
    

  def callbackRight(self,event):
    self.right_pressed = not self.right_pressed 
    

  def take_picture(self):
    print('taking picture!')
    x0 = self.tK_object.winfo_rootx()
    y0 = self.tK_object.winfo_rooty()
    x1 = x0 + self.tK_object.winfo_width()
    y1 = y0 + self.tK_object.winfo_height()
    ImageGrab.grab().crop((x0, y0, x1, y1)).save("TurtleArt.png")

  def update_movement(self):
    if self.forward_pressed:
      self.robot.Forward()
    if self.backward_pressed:
      self.robot.Backward()
    if self.left_pressed:
      self.robot.Left()
    if self.right_pressed:
      self.robot.Right() 
    