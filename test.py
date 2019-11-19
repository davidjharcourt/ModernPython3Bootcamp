nums = [1,2,3,4] 

answer = [num for num in nums if num in [3,4,5,6]]
print(answer)

# print(3 in [3,4,5,6])

# answer2 = [name[::-1].lower() for name in ["Elie","Tim","Matt"]]
# print(answer2)

numbs = [1,2,3,4,5,6]
evens = [numb for numb in numbs if numb % 2 == 0]
odds = [numb for numb in numbs if numb % 2 != 0]
print(evens)
print(odds)


#
answer =  [num for num in range(1,100) if num % 12 == 0]

answer = [letter for letter in 'amazing' if letter not in ['a','e','i','o','u']]

answer = [[i for i in range(0,10)]for num in range(0,10)]