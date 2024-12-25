from tkinter import *
from tkinter import ttk


window = Tk()
window.title("lesson 18")
window.geometry("600x500")
window.config(bg="#ffec3f")



def fun_1():
    # считываем переменную
    lab_text.config(text=num_radio.get())
    if(num_radio.get() == "b1"):
        window.config(bg="#f9ef98")
    if(num_radio.get() == "b2"):
        window.config(bg="#b7b7b7")
    if(num_radio.get() == "b3"):
        window.config(bg="#464540")




# num_radio общая переменная для связи трех Radiobutton
num_radio = StringVar()

# variable - привязка Radiobutton к переменной
radio_b1 = ttk.Radiobutton(text="button1" , variable=num_radio , value= "b1" , command=fun_1)
radio_b1.place(x=30 , y= 30)

radio_b2 = ttk.Radiobutton(text="button2" , variable=num_radio , value= "b2" , command=fun_1)
radio_b2.place(x=30 , y= 60)

radio_b3 = ttk.Radiobutton(text="button3" , variable=num_radio , value= "b3" , command=fun_1)
radio_b3.place(x=30 , y= 90)




# меняем Radiobutton
def fun_check():
    if(num_check.get()):
        # radio_b2.config(variable=num_check, value="none")
        radio_b2.config(value="none")
    else:
        radio_b2.config(value="b2")
num_check = IntVar()
check_box = Checkbutton(text="text" , variable=num_check, command=fun_check)
check_box.place(x=30 , y=180)





def fun_2():
    if(num_radio_2.get() == "b4"):
        lab_text.config(bg="#ff2020")
        check_box.config(bg="#ff2020")
    if(num_radio_2.get() == "b5"):
        lab_text.config(bg="#20ffad")
        check_box.config(bg="#20ffad")
    if(num_radio_2.get() == "b6"):
        lab_text.config(bg="#7520ff")
        check_box.config(bg="#7520ff")
num_radio_2 = StringVar()
radio_b4 = ttk.Radiobutton(text="button1" , variable=num_radio_2 , value= "b4" , command=fun_2 , style="")
radio_b4.place(x=250 , y= 30)

radio_b5 = ttk.Radiobutton(text="button2" , variable=num_radio_2 , value= "b5" , command=fun_2)
radio_b5.place(x=250 , y= 60)

radio_b6 = ttk.Radiobutton(text="button3" , variable=num_radio_2 , value= "b6" , command=fun_2)
radio_b6.place(x=250 , y= 90)





lab_text = Label()
lab_text.place(x=30 , y=150)



window.mainloop()