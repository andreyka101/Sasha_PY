

from tkinter import *


window = Tk()
window.title("lesson 25")
window.geometry("600x500")
window.config(bg="#ffec3f")



canV = Canvas(width=600 , height=500 , bg="#ffffff")
canV.place(x=0 , y=0)


canV.create_line(0,5 , 100,60 , 10,400 , 500,250 , fill="#ff3232" , width=10 , smooth=True , stipple="gray50")



canV.create_rectangle(100,100 , 400 , 300  , fill="#eeffa2" , width=6 , outline= "#720acd")



canV.create_oval(50,50 , 400 , 400  , fill="#34ffb8" , width=6 , outline= "#0e4bc3")



canV.create_rectangle(0,0 , 600 , 500  , fill="#ffffff" , width=0)



canV.create_polygon(60,100 , 400,300 , 400,100 , 60,300 , fill="#34ffb8" , width=10 , outline="#ff9e0e")








window.mainloop()


