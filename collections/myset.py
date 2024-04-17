# 1. Create Python Set
# 2. Access Set items
# 3. Add Set items
# 4. Remove Set items
# 5. Loop Sets
# 6. Join Sets
# 7. Set Methods.

# Sets are used to store multiple items in a single variable
# A set is a collection which is unordered, unchangeable but can remove items and add new items, and unindexed. No duplicates.
# Sets are written with curly brackets or using set constructor
# Sets are unordered, so you cannot be sure in which order the items will appear, cannot be referred by index or key


# myset = {"apple", "banana", "cherry"}

# print(myset)

# print(len(myset))

# It is possible to use the set() constructor to make a set
this_set = set(("apple", "avocado", "orange"))
print(this_set)
print(type(this_set))

# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop or ask if a specified value is present in a set, by using the in keyword.
for x in this_set:
  print(x)

print("banana" in this_set)
print("banana" not in this_set)

# Once a set is created, you cannot change its items, but you can add new items: add() method

this_set.add("banana")
print(this_set)

# add items from another set into the current set, use the update() method

tropical = {"pineapple", "mango", "papaya"}
print(tropical)
this_set.update(tropical)
print(this_set)

# Remove Set items
print(this_set)
this_set.remove("apple")  # raising error if the item to remove does not exist.
this_set.discard("app")   # no raising error if the item to remove does not exist
this_set.pop()            # remove random item, the return value of the pop method is the remove item
print(this_set)

# this_set.clear()    # the clear() method empties the set
# del tropical        # the del keyword will delete the set completely

# Join Sets
# the union() and update() methods joins all items from both sets
set1 = {1, "a", "b", "c", "d"}
set2 = {1, 2, 3}
set4 = {5, 6, 7}
list = ["apple", "orange"]
set3 = set1.union(set2) # or using |
set = set1 | set2 | set4
#print(set3)
print(set)
# union() method or | operator allows you to join a set with other data types, like lists or tuples
x = set1.union(list)
print(x)
# the intersection() method or & operator keeps ONLY the duplicates
# the difference() method or - operator keeps the items from the first set that are not in the other set
# the symmetric_difference() method or ^ operator keeps all items except the duplicates