from tkinter import *


window = Tk()

window.title("lesson 17")
window.geometry("600x500")


lab_text_1 = Label(text="rggjg" , font=("Arial Black" , 15) , fg="#83568d" , bg="#eaae2c")
lab_text_1.place(x=30 , y=40)



def fun():
    print('click')
    lab_text_1.place(x=300)
    but_1.config(text="super ruuun" ,bg="#2cea82" )
    # but_1.configure()
but_1 = Button(text="run" , command=fun)
but_1.place(x=30 , y=50)



window.mainloop()
print("end")