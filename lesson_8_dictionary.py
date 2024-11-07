# создание словаря
obj = {
    "key_num":50,
    "num":0,
    5:123,
    27:"i string",
    "30":[1,2,3],
}

print(obj)

obj["848484"] = 5555

print(obj)

# получаем значение по ключу
# print(obj["key_num"])
# print(obj[5])
# print(obj[27])
# print(type(obj))



# словарь это список
# obj_2 = {
#     0:"q",
#     1:"w",
#     2:"e",
#     3:"r",
#     4:"t",
#     5:"y",
# }
# print(obj_2[2])



# изменение значения по ключу
# print(obj["key_num"])
# obj["key_num"] = 10
# print(obj["key_num"])



# создание значения по ключу
## print(obj[1])
# obj[1] = 9
# print(obj[1])
# print(obj)



# удаление переменной
# num_d = 8
# print(num_d)
# del num_d
# print(num_d)



# удаление по ключу
# print(obj)
# del obj["num"]
# print(obj)

# тоже самое ,но список
# arr = [1,2,3,4]
# print(arr)
# del arr[1]
# print(arr)



# metods

# возвращает значение ключа, но если его нет возвращает None
# print(obj.get(27))
# print(obj[27])

# print(obj.get(3))
# print(obj[3])



# obj.setdefault(key, val) - возвращает значение key, но если его нет создает key со значением val или None
# print(obj.setdefault(3 , "hello"))
# print(obj)



# obj.update(dist) - обновляет словарь obj, добавляя пары словаря dist
# obj.update({
#     "i":80,
#     "w":5,
# })
# print(obj)



# возвращает список ключей
# print(obj.keys())



# возвращает список значений
# print(obj.values())



# удаляет по ключ и возвращает значение
# print(obj)
# print(obj.pop("num"))
# print(obj)



# удаляет последнюю пару и возвращает её
# print(obj)
# print(obj.popitem())
# print(obj)



# возвращает копию словаря
# obj_copy= obj.copy()
# print(obj_copy)



# очищает словарь
# obj.clear()
# print("obj =" , obj)
# print("obj_copy =" , obj_copy)



# for i in obj:
#     print("i =" , i)
#     print("obj[i] =" , obj[i])



# возвращает пары (ключ, значение) для for
# for k , v in obj.items():
#     print(k , "=" , v)






# дз
# лёгкая сложность задание 1
# создайте два словаря объедените их и выведите в консоль


# средняя сложность задание 2
# Создайте словарь, в котором ключами будут числа от 1 до 10, 
# а значениями эти же числа, возведенные в куб


# средняя сложность задание 3
# Создайте словарь из строки 'hello python' следующим образом: 
# в качестве ключей возьмите символ строки, 
# а значениями пусть будет индекс символа


# сложная сложность задание 4
# Даны два списка одинаковой длины.
# Необходимо создать из них словарь таким образом, 
# чтобы элементы первого списка были ключами, 
# а элементы второго — соответственно значениями нашего словаря.
