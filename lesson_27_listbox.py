from tkinter import *
from tkinter import ttk


window = Tk()
window.title("lesson 25")
window.geometry("900x500")
window.config(bg="#ffec3f")



lab_text = Label(text="text", font=("" , 15))
lab_text.place(x=10 , y=250)


arr = [1,2,3,4,"vdvdvdv","wwwc",5 , "qww" ,"egb",6,7,8,9,10,11]
list_box = Listbox(listvariable=Variable(value=arr) ,  font=("Arial Black" , 13))
list_box.place(x=30 , y=30 , height=200 , width=170)



def fun():
    print(list_box.curselection())
    lab_text.config(text= list_box.curselection())
but1 = Button(text="b1" , command=fun)
but1.place(x=400 , y=30)



def fun_get():
    print(list_box.get(list_box.curselection()))
    # lab_text.config(text= list_box.curselection())
but2 = Button(text="b2" , command=fun_get)
but2.place(x=400 , y=60)



window.mainloop()