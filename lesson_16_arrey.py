
# нужная ссылка
# https://pythonworld.ru/moduli/modul-array-massivy-v-python.html


from array import array

# создаём массив
# array(r , s)
# r - режим массива (размер каждой ячейки в массиве , таблица в ссылке)
# s - список (можно не писать)
arr = array("b" , [2 , 4 ,7 , 1 , 3 , 5 , 8])
# print(arr)
# print(arr[0])



# у массива есть методы списков:
# array.append(х) - добавление элемента в конец массива.
# array.count(х) - возвращает количество вхождений х в массив.
# array.extend(arr_list) - добавление элементов из списка в массив.
# array.index(х) - номер первого вхождения x в массив.
# array.insert(n, х) - включить новый пункт со значением х в массиве перед номером n. Отрицательные значения рассматриваются относительно конца массива.
# array.pop(i) - удаляет i-ый элемент из массива и возвращает его. По умолчанию удаляется последний элемент.
# array.remove(х) - удалить первое вхождение х из массива.
# array.reverse() - обратный порядок элементов в массиве.




# print(arr.typecode)



# print(arr.itemsize)



# print(arr.buffer_info())



# print(arr)
# arr.byteswap()
# print(arr)



# print(arr.tobytes())



# arr.frombytes(b'\x20\x49\x87\x11')
# arr.frombytes(bytes("\x20\x49\x87\x11" , encoding = "UTF-8"))
# print(arr)



# with open("arr_text.txt" , "bw") as file:
#     arr.tofile(file)



# with open("arr_text.txt" , "br") as file:
#     arr_2 = array("b")
#     arr_2.fromfile(file , 4)
#     print(arr_2)



# arr.fromlist([2,5,80])
# print(arr)



# arr.fromlist([2,5,80])
# print(arr)



# arr_list = arr.tolist()
# print(type(arr_list))

# arr_3 = array("b" , arr_list)
# print(arr_3)





el = arr[0]
arr[0] = arr[1]
arr[1] == el


