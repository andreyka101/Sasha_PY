
# функция возвращает функцию
# def fun_1():
#     print("start fun_1()")
#     return 3

# def fun_2():
#     print("start fun_2()")
#     return fun_1() + 1

# print(fun_2())

# print("==============")

# print(fun_1())



# рекурсия - функция возвращает саму себя
# num = 0
# def fun_3():
#     print("start fun_3()")
#     global num
#     num+=1
#     if(num == 10):
#         return 0
#     else:
#         return fun_3()

# fun_3()
# print("end")



# функция возвращает саму себя и передаёт себе же изменённое значение
# def fun_4(num):
#     print(f"start fun_4({num})")
#     print("num =" , num)
#     num -= 1
#     if(num == 0):
#         return "ok"
#     else:
#         return fun_4(num)


# print(fun_4(7))



# тоже саме, но короче
# def fun_4(num):
#     print(f"start fun_4({num})")
#     print("num =" , num)
#     if(num == 0):
#         return "not ok"
#     return fun_4(num - 1)

# print(fun_4(7))



# тоже саме, но обрабатываем дополнительную переменную num
# def fun_5(num , index = 0):
#     print(f"start fun_5({num} , {index})")
#     if(num == index):
#         return "end"
#     index += 1
#     return fun_5(num , index)

# print(fun_5(8))



# пример с переменной хронилищем
def fun_6(num , summ = 0):
    print(f"start fun_6({num} , {summ})")
    summ += num
    if(num != 0):
        return fun_6(num - 1 , summ)
    return summ
    
    
print(fun_6(10))






# дз
# номер 1
# Напишите функцию для вычисления факториала числа

# номер 2
# Напишите программу для возведения числа n в степень m. 
# нельзя использовать степень (**)

# номер 3
# напишите функцию которая принимает список и возвращает сумму всех чисел списка

# номер 4
# напишите функцию которая принимает два списка одинаковой длины.
# Необходимо создать из них словарь таким образом, 
# чтобы элементы первого списка были ключами, 
# а элементы второго — соответственно значениями нашего словаря.
# функция возвращает словарь

# номер 5
# Напишите функцию которая принимает список чисел и строк и возвращает список с удалёнными строками
if(type("4") == str):
    print("ok")
    



