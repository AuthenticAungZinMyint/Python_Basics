#lazy buttons
#demo create buttons

from tkinter import *

#create root window
root = Tk()
root.title("Lazy buttons")
root.geometry("200x90")

#Create frame in the window to hold other widgets
app = Frame(root)
app.grid()

#Create buttons in the frame
bttn1 = Button(app, text = "I do nothing")
bttn1.grid()

#Create a sec button in frame
bttn2 = Button(app)
bttn2.grid()

bttn2.configure(text = "Me too")

#create a third button
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "Same here!"

#kick off the window's event loop
root.mainloop()
