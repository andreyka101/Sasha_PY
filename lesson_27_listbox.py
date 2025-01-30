from tkinter import *



# split(x) - режет строку по x символу
s_str = 'хлеб=x1=40'
print(s_str.split("="))
print(s_str.split("=")[2])



num = [2,5,3,6]
print(f'iefihe {num}if')




window = Tk()
window.title("lesson 25")
window.geometry("900x500")
window.config(bg="#ffec3f")



lab_text = Label(text="text", font=("" , 15))
lab_text.place(x=10 , y=250)


inp = Entry()
inp.place(x=10 , y=290)



# Listbox - Отображение списка в интерфейсе 
arr = [1,2,3,4,"vdvdvdv","wwwc",5 , "qww" ,"egb",6,7,8,9,10,11]
list_box = Listbox(listvariable=Variable(value=arr) ,  font=("Arial Black" , 13))
list_box.place(x=30 , y=30 , height=200 , width=170)



def fun_index():
    # list_box.curselection() - возвращает выбранный индекс 
    print(list_box.curselection())
    lab_text.config(text= list_box.curselection())
but1 = Button(text="index" , command=fun_index)
but1.place(x=400 , y=30)



def fun_get():
    # list_box.get(i) - возвращает элемент индекса i
    lab_text.config(text= list_box.get(list_box.curselection()))
but2 = Button(text="get" , command=fun_get)
but2.place(x=400 , y=60)



def fun_del():
    # list_box.delete(i) - удаляет элемент по индексу i
    # list_box.delete(0)
    list_box.delete(list_box.curselection())
but2 = Button(text="delete" , command=fun_del)
but2.place(x=400 , y=90)



def fun_insert():
    # list_box.insert(x , element) - вставляет новый элемент на x индекс
    list_box.insert(0 , inp.get())
but2 = Button(text="insert" , command=fun_insert)
but2.place(x=400 , y=120)



def fun_rewrite():
    # list_box.insert(list_box.curselection(),"zxz")
    list_box.insert(list_box.curselection(), inp.get())
    list_box.delete(list_box.curselection())
but2 = Button(text="rewrite" , command=fun_rewrite)
but2.place(x=400 , y=150)




window.mainloop()


