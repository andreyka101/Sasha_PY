
from tkinter import *
from tkinter import ttk


window = Tk()
window.title("lesson 25")
window.geometry("900x500")
window.config(bg="#ffec3f")



lab_text = Label(text="text", font=("" , 15))
lab_text.place(x=10 , y=150)



def fun_press(event):
    # lab_text.config(text=event)
    # lab_text.config(text=event.state)
    window.title(f"{event.x} , {event.y}")

window.bind("<Motion>" , fun_press)




def fun_1(event):
    lab_text.config(text=event)

window.bind("<Button-1>" , fun_1)




def fun_2(event):
    lab_text.config(text=event)

window.bind("<Button-2>" , fun_2)




def fun_3(event):
    lab_text.config(text=event)

window.bind("<Button-3>" , fun_3)




def fun_3(event):
    lab_text.config(text=event)

window.bind("<MouseWheel>" , fun_3)




window.mainloop()