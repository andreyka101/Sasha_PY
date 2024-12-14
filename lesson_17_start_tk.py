
# импортируем библиотеку tkinter
from tkinter import *



# создаём окно 
window = Tk()
# меняем название окна
window.title("lesson 17")
# меняем ширину и высоту окна 
window.geometry("600x500")



# создаём текст через Label
# bg= цвет фона 
# fg= цвет текстам
# font = шрифт и размер текста 
lab_text_1 = Label(text="текст" , font=("Arial Black" , 15) , fg="#83568d" , bg="#eaae2c")
lab_text_1.place(x=30 , y=40)



def fun():
    print('click')
    # изменяем позиция lab_text_1
    lab_text_1.place(x=300)

    # с помощью метода configure или config можно изменить параметры объекта 
    but_1.config(text="super ruuun" ,bg="#2cea82" )
    # but_1.configure()

# создаём кнопку command вызывает функцию
but_1 = Button(text="run" , command=fun ,  font=("Arial Black" , 15))
but_1.place(x=30 , y=80)




lab_text_1 = Label(text="454554\n5ffgjj    " , font=("Arial Black" , 15) , fg="#83568d" , bg="#2ceada")
lab_text_1.place(x=300 , y=50 , height=100 , width=100)




window.mainloop()
print("end")