
from tkinter import *


window = Tk()
window.title("lesson 25")
window.geometry("500x500")
window.config(bg="#ffec3f")



lab_text = Label(text="text", font=("" , 15))
lab_text.place(x=10 , y=20)



# obj_button = {
#     "but1": Button(text="ifhfhhf")
# }
# obj_button["but1"].place(x=30 , y=60)


obj_button = {}



num = 0
def fun(event):
    print(event.widget)
    global num
    # получаем элемент 
    element = event.widget
    # получаем текст элемента
    print(element["text"])
    print(element["text"].split(" "))
    arr_text = element["text"].split(" ")
    num += int(arr_text[2])


    if(int(arr_text[2]) == 1):
        window.config(bg="#fffbd6")
    if(int(arr_text[2]) == 2):
        window.config(bg="#bab698")
    if(int(arr_text[2]) == 3):
        window.config(bg="#918e77")
    if(int(arr_text[2]) == 4):
        window.config(bg="#6d6b5c")
    if(int(arr_text[2]) == 5):
        window.config(bg="#555344")
    if(int(arr_text[2]) == 6):
        window.config(bg="#38372f")
    if(int(arr_text[2]) == 7):
        window.config(bg="#0c0c0a")


    
    
    lab_text.config(text=num)

    


for i in range(1 , 7+1):
    obj_button[f"but-{i}"] = Button(text = f"click + {i}")
    obj_button[f"but-{i}"].place(x=30 , y=60 * i)
    obj_button[f"but-{i}"].bind("<Button-1>" , fun)





window.mainloop()