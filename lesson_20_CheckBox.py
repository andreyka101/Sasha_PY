from tkinter import *


window = Tk()
window.title("lesson 18")
window.geometry("600x500")
window.config(bg="#ffec3f")



def fun():
    lab_text.config(text=num_check.get())
    if(num_check.get()):
        window.config(bg="#ffffff")
    else:
        window.config(bg="#000000")

        # закрытия окна
        # window.destroy()


# в num_check хранится положения Checkbutton
num_check = IntVar()

# Checkbutton это кнопка с двумя положениями
check_box = Checkbutton(text="text" , variable=num_check, command=fun)
check_box.place(x=30 , y=30)
num_check_2 = IntVar()
check_box_2 = Checkbutton(text="text2" , variable=num_check_2, command=fun)
check_box_2.place(x=30 , y=60)



lab_text = Label(text=num_check.get() , font=("Arial Black" , 15) , fg="#0afff3" , bg="#ea2c65")
lab_text.place(x=40 , y=100)



window.mainloop()