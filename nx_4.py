from tkinter import *
from tkinter import ttk


window = Tk()
window.title("lesson 25")
window.geometry("900x500")
window.config(bg="#ffec3f")



lab_text = Label(text="text", font=("" , 15))
lab_text.place(x=10 , y=150)



def fun_press(event):
   
    
    window.title(f"{event.x} , {event.y}")
window.bind("<Motion>" , fun_press)




def fun_1(event):
   
    lab_text.config(text=event)
window.bind ("<Button-4>",fun_1)




def fun_press(event):
    def fun_x(event):

        window.config(bg="#08c6cd")
        lab_text.config(text=event)

    global x
    x = window.bind("<KeyPress>" , fun_x)


window.bind("<Button-1>" , fun_press)


def fun_release(event):
    del x

window.bind("<KeyRelease>" , fun_release)







window.mainloop()