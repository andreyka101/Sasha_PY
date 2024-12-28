from tkinter import *

window = Tk()
window.title("lesson 18")
window.geometry("600x500")
window.config(bg="#4c3fff")


num_menu = Menu(tearoff=0)
num_menu.add_command(label="n1")
num_menu.add_command(label="n2")
num_menu.add_command(label="n3")


def fun():
    window.config(bg="#4e4e4e")
main_menu = Menu()
main_menu.add_command(label="123" , command=fun)


file_menu = Menu(tearoff=0)

file_menu.add_command(label="sive")

num_check = IntVar()
file_menu.add_checkbutton(label="check" ,variable=num_check)

file_menu.add_separator()


def fun_2():
    print(num_radio.get())
num_radio = StringVar()
file_menu.add_radiobutton(label="radio1" , variable=num_radio , value= "b1" , command=fun_2)
file_menu.add_radiobutton(label="radio2" , variable=num_radio , value= "b2" , command=fun_2)
file_menu.add_radiobutton(label="radio3" , variable=num_radio , value= "b3" , command=fun_2)


file_menu.add_cascade(menu=num_menu , label="num" , command=fun)




main_menu.add_cascade(label="file" , menu=file_menu)
main_menu.add_cascade(label="num" , menu=num_menu)


window.config(menu=main_menu)

window.mainloop()