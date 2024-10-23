arr = [1 , 2 , 3 , 4 , 5 , 3 , 6]
print(arr)

# arr.append(555)
print(arr)


# arr.append([9,8,7])
print(arr)


# arr.extend([9,8,7])
print(arr)


arr.insert(2,"uou")
print(arr)


print(arr.count(3))


print(arr.index(3))

print(arr.index(3 , 4))


arr.remove("uou")
print(arr)


print("arr.pop(0) =" , arr.pop(0))
print(arr)

print("arr.pop() =" , arr.pop())
print(arr)


arr = [8,4,3,8,3,1]
print(arr)
arr.sort()
print(arr)


arr.reverse()
print(arr)


# arr.clear()
# arr = []
# arr = None
print(arr)
print(type(arr))


arr_2 = arr
arr_copy = arr.copy()

print("arr =" , arr)
print("arr_2 =" , arr_2)
print("arr_copy =" , arr_copy)

arr.clear()
print("===============")

print("arr =" , arr)
print("arr_2 =" , arr_2)
print("arr_copy =" , arr_copy)





