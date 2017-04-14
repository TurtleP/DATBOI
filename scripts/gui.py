from tkinter import *
from tkinter import messagebox

#Define the frame
top = Tk()
top.resizable(width=False, height=False)
top.geometry('{}x{}'.format(500, 250)) #Formatted as W * H
top.wm_title("Here Come DATBOI!")

#Add a label to the frame
label = Label(top, text="Oh shit, what up?")
label.pack()

#Add a button to the frame
def killswitchEngage():
    messagebox.showinfo("Execute Order 66", "It will be done, my lord")
killswitch = Button(top, text="Order 66", command=killswitchEngage)
killswitch.pack()

top.mainloop()