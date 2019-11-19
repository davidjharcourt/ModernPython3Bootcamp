import pdb

first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)

# import pdb
#pbd.set_trace()
# import pdb; pbd.set_trace()

# Common pdb commands
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)