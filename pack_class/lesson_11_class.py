
class Dogs():
    num_2_str = "ffe"
    def __init__(self , nume_loc):

        print("start Dogs")

        self.num_1 = 12
        num_1 = 3
        # print(num_1)
        # print(self.num_1)

        self.num_2_str = "uuqw"

        self.nume = nume_loc
    
    def run(self):
        print("run run run run")
    def get_nume(self):
        print("hello I" , self.nume)
    def super_num_1(self, x):
        self.num_1 += x

        self.run()



dog_1 = Dogs("sharick")

# print(dog_1.num_1)
# print(dog_1.num_2_str)



# print(Dogs.num_2_str)
# print(Dogs().num_2_str)



# print(Dogs)
# print(Dogs())
# print("=====type=====")
# print(type(Dogs))
# print(type(Dogs()))



# dog_1.run()

# print(dog_1.run)
# print(dog_1.run())



# dog_1.get_nume()



# dog_2 = Dogs("wwwww")
# dog_1.get_nume()
# dog_2.get_nume()



print(dog_1.num_1)
dog_1.super_num_1(10)
dog_1.super_num_1(8)
print(dog_1.num_1)


