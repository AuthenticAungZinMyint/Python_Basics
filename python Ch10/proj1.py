#simple GUI
#demo creating a window

from tkinter import *

#create root window
root = Tk()

#modify the window
root.title("Simple GUI")
root.geometry("200x100")

#kick off the window's event loop
root.mainloop()
