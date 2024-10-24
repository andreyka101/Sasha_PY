arr = [1 , 2 , 3 , 4 , 5 , 3 , 6]
print(arr)


# arr.append(x) - Добавляет элемент x в конец списка
# arr.append(555)
print(arr)
# arr.append([9,8,7])
print(arr)


# arr.extend(x) - Расширяет список arr, добавляя в конец все элементы списка x
# arr.extend([9,8,7])
print(arr)


# arr.insert(i, x) - Вставляет на i-ый элемент значение x
arr.insert(2,"uou")
print(arr)


# arr.count(x) - Возвращает количество элементов со значением x
print(arr.count(3))


# arr.index(x, i) - Возвращает положение первого элемента со значением x поиск начинается с индекса i (можно не писать)
print(arr.index(3))
print(arr.index(3 , 4))


# arr.remove(x) - Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
arr.remove("uou")
print(arr)


# arr.pop(i) - 	Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
print("arr.pop(0) =" , arr.pop(0))
print(arr)
print("arr.pop() =" , arr.pop())
print(arr)


# arr.sort() - Сортирует список
arr = [8,4,3,8,3,1]
print(arr)
arr.sort()
print(arr)


# arr.reverse() - Разворачивает список
arr.reverse()
print(arr)


# arr.clear() - Очищает список
# arr.clear()
# arr = []
# arr = None
print(arr)
print(type(arr))


arr_2 = arr
arr_copy = arr.copy()



# arr.copy() - Поверхностная копия списка
print("arr =" , arr)
print("arr_2 =" , arr_2)
print("arr_copy =" , arr_copy)

arr.clear()
print("===============")

print("arr =" , arr)
print("arr_2 =" , arr_2)
print("arr_copy =" , arr_copy)





# dz
# https://metanit.com/python/practice/4.php
# https://pythonist.ru/python-spiski-zadachi-dlya-nachinayushhih/
