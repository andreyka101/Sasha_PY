arr = [1,2,3,4]
print(arr)
print(arr[0])
num = arr[2] + 6
print(num)



for i in arr:
    print(i)


# num_2 = None
# print(num_2)


arr_2 = [2 , 4.5 , True , None , "str" , [4,5,7]]
print(arr_2)


arr_3 = [
    [3,4,8,5,9],
    [2,4,7,2,1],
    [1,2,3,4,5]
]
print(arr_3[0][2] , arr_3[2][3])


for element_arr in arr_3:
    print(element_arr)
    for i in element_arr:
        print(i)
print(arr_3)


arr_4 = [5,4,3,2,1]
print(arr_4)
arr_4[0] = 0
print(arr_4)


for x in range(len(arr_3)):
    print(x)
    for y in range(len(arr_3[x])):
        arr_3[x][y] *= 2
print(arr_3)


arr_5 = [1,2,3]
arr_5.append(45)
print(arr_5)
arr_5.remove(45)
print(arr_5)

