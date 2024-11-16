

class Animals():
    """это класс"""
    def __init__(self , nume_loc):
        print("start Animals")
        self.num = 5
        self.__num_p = 12
        self.nume = nume_loc
        self.__p_method()
    def get_num_p(self):
        '''feeee'''
        return self.__num_p
    def __p_method(self):
        print("i private method")



# ani_obj = Animals("1234")


# print(ani_obj.num)
# ani_obj.num = [9,3,2,6]
# print(ani_obj.num)



# print(ani_obj.__num_p)
# ani_obj.__num_p = 0
# print(ani_obj.__num_p)
# print(ani_obj.get_num_p())



# ani_obj.__p_method()





class Cats(Animals):
    def __init__(self , name_cat):
        super().__init__(name_cat)
        self.wer = 6
    def may_p(self):
        print("may may may")




num_cat = Cats("wwwww")










