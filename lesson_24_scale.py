
from tkinter import *
from tkinter import ttk


window = Tk()
window.title("lesson 18")
window.geometry("600x500")
window.config(bg="#ffec3f")



lab_text = Label()
lab_text.place(x=30 , y=150)



def fun_s(event):
    lab_text.config(text=event)

    # print(type(event))

    # print(int(float(event)) + 20)

    # lab_text.place(x=event)
    # scale_n1.place(y=event)


scale_n1 = Scale(orient=HORIZONTAL , bg="#79ffac" , command=fun_s , length=200 , from_=0 , to=10 )
scale_n1.place(x=70 , y=40)



scale_n2 = ttk.Scale(orient= VERTICAL, command=fun_s , length=200 , from_=0 , to=5 , value=3)
scale_n2.place(x=300 , y=40)




def fun_b():
    but.config(text= scale_n1.get())
but = Button(text="click", command=fun_b)
but.place(x=10,y=10)



window.mainloop()