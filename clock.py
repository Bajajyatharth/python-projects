import time
from tkinter import *

root=Tk()
root.title("clock")

def present_time():
    display_time = time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(10,present_time)

digi_clock=Label(root,font=("Helvetica",100,"bold italic"),bg="grey",fg="black")
digi_clock.pack()

present_time()

root.mainloop()