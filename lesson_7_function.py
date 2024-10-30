# def fun_1():
#     print("hello fun_1")

# fun_1()
# fun_1()
# print("end")



# num = 8
# def fun_2():
#     print(2 + num)

# fun_2()



# num_2 = 8
# def fun_3():
#     num_3 = 2
#     print(num_3)
#     num_3 = num_3 + 2
#     print(num_3)
#     num_2 = 0
#     print("local num_2 =", num_2)

# print(num_2)
# fun_3()
# print(num_2)



# def fun_4():
#     num_4 = 5
#     # num_5 = 7
#     # num_6 = 2
#     return num_4


# print(fun_4())



# def fun_5():
#     print("hello")
#     return 0
#     print("world")

# print(fun_5())



# def fun_6(x):
#     print(x)
#     return x * 10

# print(fun_6(5))



# def fun_7(x , y):
#     print(x , y)
#     return 10

# print(fun_7(5 , 6))



# def fun_8(num = 1):
#     print(num)

# fun_8()



# def fun_8(x , y , z = 50):
#     print(x , y , z)

# fun_8(1,2)



# num_5 = 9
# def fun_9():
#     global num_5
#     num_5 = 4
#     print("fun =" , num_5)

# print(num_5)
# fun_9()
# print(num_5)



num_6 = 1
def fun_10():
    global num_6
    num_6 = num_6 + 1

print(num_6)
fun_10()
fun_10()
fun_10()
fun_10()
print(num_6)

