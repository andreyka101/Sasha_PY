
from tkinter import *


window = Tk()
window.title("lesson 25")
window.geometry("500x500")
window.config(bg="#ffec3f")



canV = Canvas(width=600 , height=500 , bg="#ffffff")
canV.place(x=0 , y=0)
canV.create_line(0 , 5  , 100 ,60)


window.mainloop()