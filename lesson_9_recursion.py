
# def fun_1():
#     print("start fun_1()")
#     return 3

# def fun_2():
#     print("start fun_2()")
#     return fun_1() + 1

# print(fun_2())

# print("==============")

# print(fun_1())



# num = 0
# def fun_3():
#     print("start fun_3()")
#     global num
#     num+=1
#     if(num == 10):
#         return 0
#     else:
#         return fun_3()

# fun_3()
# print("end")



# def fun_4(num):
#     print(f"start fun_4({num})")
#     print("num =" , num)
#     num -= 1
#     if(num == 0):
#         return "ok"
#     else:
#         return fun_4(num)


# print(fun_4(7))



# def fun_4(num):
#     print(f"start fun_4({num})")
#     print("num =" , num)
#     if(num == 0):
#         return "not ok"
#     return fun_4(num - 1)

# print(fun_4(7))



# def fun_5(num , index = 0):
#     print(f"start fun_5({num} , {index})")
#     if(num == index):
#         return "end"
#     index += 1
#     return fun_5(num , index)

# print(fun_5(8))



def fun_6(num , summ = 0):
    print(f"start fun_6({num} , {summ})")
    summ += num
    if(num != 0):
        return fun_6(num - 1 , summ)
    return summ
    
    
print(fun_6(10))





    



