# def fun_1(x):
#     return x * 2

# print(fun_1(3))
# print(fun_1)



# создание лямбды
# лямбда всегда возвращает значение
# lam_1 = lambda: 8
# print(lam_1())
# print(lam_1)



# lam_2 = lambda: 12 * 3
# print(lam_2())
# print(lam_2())
# print(lam_2())



# использование глобальной переменной
# num = 4
# lam_3 = lambda: num + 8
# print(lam_3())



# передача лямбде значения
# lam_4 = lambda x: x * 3
# print(lam_4(8))



# передача лямбде несколько значений
# lam_5 = lambda x , y: x + y
# print(lam_5(8 , 1))



# использование метода
# arr_x = [1,2,3,4]
# lam_6 = lambda: arr_x.pop(3)
# print(lam_6())
# print(arr_x)



# значение по умолчанию в лямбде
# lam_7 = lambda x = 5: x + 1
# print(lam_7())



# условие
# num_int = 7
# if(num_int < 5):
#    num_str_if = "yes" 
# else:
#    num_str_if = "not" 
# print(num_str_if)



# тоже самое условие но в одну строку
# num_int_2 = 3
# num_str_if_2 = "yes" if(num_int_2 < 5) else "not"
# print(num_str_if_2)



# если условие выполняется то вернёт лямбду
# num_int_3 = 3
# num_str_if_3 = lambda x: x * 3 if(num_int_3 < 5) else "not"
# print(num_str_if_3(3))
   


# условие в лямбде
# lam_8 = lambda x , y = 0 : y if(x < y) else x * y
# print(lam_8(2,9))
# print(lam_8(20,4))



# map(fun, arr) - использует функцию fun к каждому элементу arr
# def fun_2(x):
#     return x * 2
# arr = [1,2,3,4,5]
# чтобы map корректно работала её нужно вызывать в функции list
# arr_2 = list(map(fun_2 , arr))
# print(arr_2)



# map - принимает до шесть списков
# lambda x, y - x элемент первого списка , y элемент второго списка
# def fun_2(x , w):
#     return x + w
# arr3 = [1,2,3,4,5]
# arr4 = [9,6,4,9,7]
# arr_n = list(map(fun_2 , arr3 , arr4))
# print(arr_n)



# использование лямбды в функции map
# arr_5 = [1,2,3,4,5]
# arr_5 = list(map(lambda x: x - 5 , arr_5))
# print(arr_5)



# filter - он фильтрует
# arr_6 = [1,2,3,4,5 , 6]
# arr_6 = list(filter(lambda x: x < 4  , arr_6))
# print(arr_6)







# дз
# задачи на лямбду (lambda):
# номер 1
# дан список чисел все числа которые равны 1, 2, 3 должны стать числом 0 

# номер 2
# дан список чисел и строк убрать все строки из списка

# номер 3
# даны два списка чисел которые имеют одинаковый размер 
# написать программу которая сравнивает элемент каждого списков и сохраняет самый большой
# пример: 
#     даны списки
#         ar1 = [1,3,6]
#         ar2 = [3,9,2]
#         ответ : [3,9,6]

# номер 4
# дан список в котором списки с числами ,каждое число списка умножить на num
# переменная num прибавляется на 1 с каждым новым списком (num изначально равен 2)




