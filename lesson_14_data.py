
# открытие файла
# file_1 = open("file_las_1.txt")
# print(file_1)



# режимы открытия:
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись



# по умолчанию файл открывается в режиме 'r'
# file_2 = open("file_las_1.txt" , "r")
# .read() - получаем текст отрытого файла
# print(file_2.read())
# print(file_2)



# переписываем файл
# file_3 = open("file_las_1.txt" , "w")
# .write() - запись
# file_3.write("2e2eee")
# .close() - закрывает файл
# file_3.close()


# если не закрыть файл то чтение не сработает
# print(open("file_las_1.txt").read())



# with - сам закрывает файл 
# with open("file_las_1.txt" , "a") as file:
#     file.write("880001")

# print(open("file_las_1.txt").read())



# print("1234\n5678")


# with open("file_las_1.txt" , "r" , encoding="UTF-8") as file:
    # print(file.read())
    # print([file.read()])


    # метод .readlines() каждую строку txt файла превращает в элемент массива
    # print(file.readlines())
    
    
    # print("123+123+efff+sss+wwwww+5".split("+"))
    # file_read = file.read()
    # .split(s) - разделяет строку по строке s
    # print(file_read.split("\n"))



# with open("papka_filse/file2_les.txt" , "r") as file:
#     print(file.read())








# дз
# номер 1
# сделать программу , которая принимает текст и сохраняет в файл 


# номер 2
# сделать программу калькулятор с историей программа должна показывать историю


# номер 3
# создайте менеджер пользователей
# . программа должна работать до тех пор пока не не будет введено exit или ex
# . если ввести new - создаётся новый пользователь он должен хранить имя и пароль (если ввести существующие имя то программа просит его изменить)
# . если ввести del - удаляется пользователь его имя и пароль
# все пользователи должны сохраняются на txt файл






# with open("C:/main_brain/del_file_global_2.txt" , "r") as file:
#     print(file.read())



# with open("./papka_filse/file2_les.txt" , "r") as file:
#     print(file.read())



# with open("../del_file_global.txt" , "r") as file:
#     print(file.read())



# with open("../../del_file_global_2.txt" , "r") as file:
#     print(file.read())



# with open("../../del_file_global_2.txt" , "r") as file:
#     print(file.read())



# with open("../../фаилы/../фаилы/../фаилы/../фаилы/del_s.txt" , "r") as file:
#     print(file.read())