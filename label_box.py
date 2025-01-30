
from tkinter import *


window = Tk()
window.title("lesson 25")
window.geometry("500x500")
window.config(bg="#ffec3f")



lab_1 = Label(bg="#ff1a1a")
lab_1.place(x=0 , y =0 , width=250 , height=250)

lab_2 = Label(bg="#fff41a")
lab_2.place(x=250 , y =0 , width=250 , height=250)

lab_3 = Label(bg="#63ff1a")
lab_3.place(x=0 , y =250 , width=250 , height=250)

lab_4 = Label(bg="#1ae4ff")
lab_4.place(x=250 , y =250 , width=250 , height=250)



lab_text = Label(text="text", font=("" , 15))
lab_text.place(x=150 , y=150)



# print(lab_text)
# print(type(lab_text))



def fun_motion(event):
    # получаем элемент
    # element = event.widget
    # lab_text.config(text=element)
    window.title(f"{event.x} , {event.y}")
window.bind("<Motion>" , fun_motion)



def fun_1(event):
    # получаем элемент
    element = event.widget
    print(type(element))

    if(str(element) == ".!label" or str(element) == ".!label2" or str(element) == ".!label3" or str(element) == ".!label4"):
        element.config(bg="#8314af")

    lab_text.config(text=element)
window.bind("<Button-1>" , fun_1)



def fun_3(event):
    element = event.widget

    if(str(element) == ".!label" or str(element) == ".!label2" or str(element) == ".!label3" or str(element) == ".!label4"):
        element.config(bg="#cc7497")

    lab_text.config(text=element)
window.bind("<Button-3>" , fun_3)




window.mainloop()