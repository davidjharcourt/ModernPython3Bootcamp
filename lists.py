# demo_list = [1, "David", True, None, 1979]
# print(demo_list)
# print(len(demo_list))

# r = range(1,10)
# print(list(r))

# print(demo_list[1])
# print("David" in demo_list)

# for value in demo_list:
# 	print(value)

# # i=0
# # while i < len(demo_list):
# # 	print(demo_list[i])
# # 	i += 1

# i=0
# while i < len(demo_list):
# 	print(f"{i}: {demo_list[i]}")
# 	i += 1

# first_list = [1, 2, 3, 4]
# first_list.append(5)
# print(first_list)

# first_list.extend([6,7,8,9])
# print(first_list)

# first_list.insert(4,"Middle")
# print(first_list)

# first_list = [1, 2, 3, 4]
# first_list.clear()
# print(first_list)

# first_list = [1, 2, 3, 4]
# first_list.pop()
# print(first_list)
# first_list.pop(1)
# print(first_list)

# first_list = [1, 2, 3, 4, 4, 4]
# first_list.remove(2)
# print(first_list)
# first_list.remove(4)
# print(first_list)

# numbers = [5, 5, 6, 7, 5, 8, 8, 9, 10]
# # index gives the index of an item in a list, and can
# # be give a start and stop point
# numbers.index(5)
# numbers.index(5,1)
# numbers.index(5,2)
# numbers.index(8,6,8)

# # count returns the number of times x appears in a list
# new_nums = [1, 2, 3, 3, 5, 7, 7, 9, "David", "David"]
# print(new_nums.count("David"))

# # reverse the elements of the list(in-place)
# names = ["Bob","Dan","Dave"]
# names.reverse()
# print(names)

# # sort the items of the list (in place)
# another_list = [6, 4, 1, 2, 5]
# another_list.sort()
# print(another_list)

# join - a string method, often used to convert lists to 
# strings. Concatenates a copy of the base string between 
# the strings in a list
words = ['Coding', 'is', 'fun!']
print(' '.join(words))
