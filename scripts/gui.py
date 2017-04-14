from tkinter import *
top = Tk()
top.resizable(width=False, height=False)
top.geometry('{}x{}'.format(500, 250)) #Formatted as W * H
top.wm_title("Here Come DATBOI!")
label = Label(top, text="Oh shit, what up?")
label.pack()
top.mainloop()