from tkinter import*
from turtle_robot import TurtleRobot
from control import ControlInterface


def RunSimulation():
  window = Tk()                             
  bob = TurtleRobot("Bob","red")
  ControlInterface(window,bob)
  window.mainloop()

if __name__ == "__main__":
    # execute only if run as a script
    RunSimulation()
