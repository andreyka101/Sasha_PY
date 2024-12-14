from tkinter import *


window = Tk()
window.title("lesson 18")
window.geometry("600x500")
window.config(bg="#ffec3f")



ent_inp = Entry(font=("Arial Black" , 10) ,bg="#8f8100" ,fg="#faf2a8" , width=20 )
ent_inp.place(x=30 , y=30)



def fun():
    print(ent_inp.get())
    # print(int(ent_inp.get()) + 5)
    lab_text.config(text = ent_inp.get())
but_1 = Button(text="get text" , command=fun ,  font=("Arial Black" , 15))
but_1.place(x=30 , y=80)

lab_text = Label(text="текст22" , font=("Arial Black" , 15) , fg="#fffb0a" , bg="#3c2cea")
lab_text.place(x=230 , y=30)




def fun_2():
    ent_inp.delete(0,1)
but_2 = Button(text="clear text" , command=fun_2 ,  font=("Arial Black" , 15))
but_2.place(x=30 , y=150)




window.mainloop()