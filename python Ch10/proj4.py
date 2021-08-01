#lazy buttons 2.0
#Demo using class with tkinter

from tkinter import *

class Application(Frame):
    """ A GUI appilication with three buttons """
    def __init__(self, master):
        """ Initialize the frame """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create three buttons that do nothing """
        #create first button
        self.bttn1 = Button(self, text = "I do nothing")
        self.bttn1.grid()

        #create sec button
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Me too")

        #create third button
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Same Here"

#main
root = Tk()
root.title("Lazy buttons")
root.geometry("200x90")

app = Application(root)

root.mainloop()
        
