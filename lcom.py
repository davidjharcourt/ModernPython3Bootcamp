nums=[1,2,3]

print([x*10 for x in nums])

numbers = [1,2,3,4,5]
doubled_numbers = [num*2 for num in numbers]

print(doubled_numbers)

name = 'david'
print([char.upper() for char in name])

friends = ['clara','natalie','greta']
print([friend[0].upper() for friend in friends])

[num*10 for num in range(1,6)]

numbers = [1,2,3,4,5]

string_list = [str(num) for num in numbers]

numbs = [1,2,3,4,5,6]
evens = [numb for numb in numbs if numb % 2 == 0]
odds = [numb for numb in numbs if numb % 2 != 0]
print(evens)
print(odds)

with_vowels = "This is so much fun!"

print(''.join(char for char in with_vowels if char not in "aeiou"))[