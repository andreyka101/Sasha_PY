

class Animals():
    """это сообщение"""
    def __init__(self , nume_loc):
        print("start Animals")
        self.num = 5
        # пишем в начале __ для создания приватной переменной или метода
        self.__num_p = 12
        self.nume = nume_loc
        self.__p_method()
    def get_num_p(self):
        '''это сообщение для метода'''
        return self.__num_p
    def __p_method(self):
        print("i private method")



# ani_obj = Animals("1234")


# print(ani_obj.num)
# ani_obj.num = [9,3,2,6]
# print(ani_obj.num)



# приватная переменная
# print(ani_obj.__num_p)
# ani_obj.__num_p = 0
# print(ani_obj.__num_p)
# print(ani_obj.get_num_p())



# ani_obj.__p_method()





# наследуем класс Animals
# в наследуемом классе можно создавать свои переменные и методы
class Cats(Animals):
    def __init__(self , name_cat):
        # вызываем метод
        super().__init__(name_cat)
        self.wer = 6
    def may_p(self):
        print("may may may")




num_cat = Cats("wwwww")






# дз
# задание 1
# создайте родительский класс , описывающий транспорт
# (модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации о транспорте.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# наследуйте класс автомобили в котором есть ещё одна переменная количество мест

# наследуйте класс вертолеты с дополнительным методом взлет 



