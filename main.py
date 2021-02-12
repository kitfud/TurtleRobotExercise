from tkinter import*
from turtle_robot import TurtleRobot
from control import ControlInterface


def RunSimulation():
  turtle_window = Tk()
  turtle_window_canvas = Canvas(turtle_window, width=500, height=500)
  turtle_window_canvas.pack()

  control_window = Tk()
  control_window_canvas = Canvas(control_window, width=200, height=500)
  control_window_canvas.pack()


  bob = TurtleRobot("Bob","red",turtle_window_canvas)
  ControlInterface(turtle_window,control_window_canvas,bob)
  
  control_window.mainloop()

if __name__ == "__main__":
    # execute only if run as a script
    RunSimulation()
