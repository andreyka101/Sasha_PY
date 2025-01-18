from tkinter import *
from tkinter import ttk


window = Tk()
window.title("lesson 18")
window.geometry("600x500")
window.config(bg="#ffec3f")



lab_text = Label()
lab_text.place(x=30 , y=150)

def fun_s1(event):
    line_1.place(x = event)
def fun_s2(event):
    line_2.place(y = event)


line_1 = Label(bg="#000")
line_1.place(x=300 , y=50 , height=100 , width=3)

line_2 = Label(bg="#420202")
line_2.place(x=250 , y=100 , height=3 , width=100)


scale_n1 = ttk. Scale(orient=HORIZONTAL ,   command=fun_s1 , length=200 , from_=200 , to=400 )
scale_n1.place(x=220 , y=240)



scale_n2 = ttk.Scale(orient= HORIZONTAL,   command=fun_s2 , length=200 , from_=0 , to=200 , value=200)
scale_n2.place(x=310 , y=300)



def fun_b():
       but.config(text= scale_n1.get())
but = Button(text="ровно", command=fun_b)
but.place(x=40,y=10)



window.mainloop()