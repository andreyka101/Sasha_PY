import json


arr = [1,2,3]
json_arr_s = json.dumps(arr)
# print(type(arr))
# print(json_arr_s)
# print(type(json_arr_s))



# перезапись файла json
# with open("file_j_1.json" , "w") as file:
#     file.write(json_arr_s)



# json.loads - переводит json строку в list или dict
# arr_super = json.loads(json_arr_s)
# print(type(arr_super))
# print(arr_super[0])



# json.load - переводит открытый файл в list или dict
# with open("file_j_1.json" , "r") as file:
#     arr_2 = json.load(file)
#     print(arr_2[0])
#     print(type(arr_2))



# пример со словарем
# obj = {
#     'qwe':123,
#     "23":21,
#     56:"sttegg",
# }
# json.dump(x , f) - записывает x список или словарь в f файл
# with open("file_j_1.json" , "w") as file:
#     json.dump(obj , file)




# дз с урока 14
# номер 3
# создайте менеджер пользователей
# . программа должна работать до тех пор пока не не будет введено exit или ex
# . если ввести new - создаётся новый пользователь он должен хранить имя и пароль (если ввести существующие имя то программа просит его изменить)
# . если ввести del - удаляется пользователь его имя и пароль
# все пользователи должны сохраняются на txt файл



