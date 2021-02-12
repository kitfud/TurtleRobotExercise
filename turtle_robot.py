import turtle

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