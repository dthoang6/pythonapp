#1. Create: store data in key: value pairs, ordered, changeable, no duplicates
#2. Access
#3. Change
#4. Add
#5. Remove
#6. Loop
#7. Copy
#8. Nested
#9. Methods  

#1. Create: store data in key: value pairs, ordered, changeable, no duplicates
# dict are defined as objects with the data type <class 'dict'>
this_dict = {         # the values in dictionary items can be of any data type
  "brand": "Ford",
  "model": "Mustang",  # cannot have two items with the same key, overwrite
  "year": 1994,          # existing values
  "electric": False,
  "color": ["red", "white", "blue"]
}
# create a dict use dict() constructor
person = dict(
  name = "Dat",
  age = "34",
  country = "USA"
)
print(this_dict)
print(person)

#2. Access the items of a dictionary by referring to its key name, inside [] or using get() method
name = person["name"]
print(name)

print(person.get("age")) # get() method

x = person.keys() # the key() method will return a list of all the keys in the dict
print(x)

y = person.values() # return a list of all values in the dict
print(y)

z = person.items()  # return each item in a dictionary, as tuples in a list
print(z)

#3. Change
#4. Add
#5. Remove
#6. Loop
#7. Copy
#8. Nested
#9. Methods  