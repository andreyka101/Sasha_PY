from tkinter import *
from tkinter import ttk

window = Tk()
window.title("lesson 18")
window.geometry("600x500")
window.config(bg="#4c3fff")
def fun_1():

    lab_text.config(text=num_radio.get())
    if(num_radio.get() == "b1"):
        window.config(bg="#f9ef98")
    if(num_radio.get() == "b2"):
        window.config(bg="#b7b7b7")
    if(num_radio.get() == "b3"):
        window.config(bg="#464540")

def fun_3():
    ent_inp.delete()
but_3 = Button(text="cколько дней в неделе???" , command=fun_3 ,  font=("Arial Black" , 6))
but_3.place(x=10 , y=10)

def fun_3():
    ent_inp.delete()
but_3 = Button(text="сколько дней в году??" , command=fun_3 ,  font=("Arial Black" , 6))
but_3.place(x=200 , y=10)


def fun_3():
    ent_inp.delete()
but_3 = Button(text="при какой температуре закипает вода??" , command=fun_3 ,  font=("Arial Black" , 7))
but_3.place(x=400 , y=10)








num_radio = StringVar()


radio_b1 = ttk.Radiobutton(text="6" , variable=num_radio , value= "b1" , command=fun_1)
radio_b1.place(x=30 , y= 30)

radio_b2 = ttk.Radiobutton(text="7" , variable=num_radio , value= "b2" , command=fun_1)
radio_b2.place(x=30 , y= 60)

radio_b3 = ttk.Radiobutton(text="6" , variable=num_radio , value= "b3" , command=fun_1)
radio_b3.place(x=30 , y= 90)

radio_b4 = ttk.Radiobutton(text="10" , variable=num_radio , value= "b4" , command=fun_1)
radio_b4.place(x=30 , y= 120)



radio_b5 = ttk.Radiobutton(text="365" , variable=num_radio , value= "b5" , command=fun_1)
radio_b5.place(x=200 , y= 30)

radio_b6 = ttk.Radiobutton(text="366" , variable=num_radio , value= "b6" , command=fun_1)
radio_b6.place(x=200 , y= 60)

radio_b7 = ttk.Radiobutton(text="228" , variable=num_radio , value= "b7" , command=fun_1)
radio_b7.place(x=200 , y= 90)

radio_b8 = ttk.Radiobutton(text="1488" , variable=num_radio , value= "b8" , command=fun_1)
radio_b8.place(x=200 , y= 120)


radio_b9 = ttk.Radiobutton(text="100" , variable=num_radio , value= "b9" , command=fun_1)
radio_b9.place(x=400 , y= 30)

radio_b10 = ttk.Radiobutton(text="50" , variable=num_radio , value= "b10" , command=fun_1)
radio_b10.place(x=400 , y= 60)

radio_b11 = ttk.Radiobutton(text="88" , variable=num_radio , value= "b11" , command=fun_1)
radio_b11.place(x=400 , y= 90)

radio_b12 = ttk.Radiobutton(text="-134" , variable=num_radio , value= "b12" , command=fun_1)
radio_b12.place(x=400 , y= 120)

def fun_check():
    if(num_check.get()):
        # radio_b2.config(variable=num_check, value="none")
        radio_b2.config(value="none")
    else:
        radio_b2.config(value="b2")
num_check = IntVar()
check_box = Checkbutton(text="проверка" , variable=num_check, command=fun_check)
check_box.place(x=30 , y=180)



window.mainloop()