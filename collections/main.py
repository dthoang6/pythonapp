# collection = single "variable" used to store multiple values

# List = [] ordered and changeable. Duplicates ok
# Tuple = () ordered and unchangeable. Duplicates ok. Faster

fruit = 'avocado'

fruits = ['apple', 'orange', 'banana', 'coconut']

print(fruits)

print(fruits[1]) # index access
print(fruits[1:3]) # index access

for x in fruits:
  print(x)

# print(dir(fruits))  # list of method can use for List 
# print(help(fruits)) # description of all methods and attributes

print(len(fruits))

print('pineapple' in fruits)  # Finding Items in Lists with the in Operator
print('apple' in fruits)  # Finding Items in Lists with the in Operator

fruits[0] = 'avocado' # changeable

print(fruits)
fruits.append('banana')
print(fruits)

fruits.remove('orange')
print(fruits)

fruits.insert(1, 'orange')
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits.index('banana'))


print(fruits.count('banana'))

print(help(fruits))

# fruits.clear()
print(fruits)
