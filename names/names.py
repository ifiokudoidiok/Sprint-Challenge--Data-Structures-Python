import time

from binary_search_tree import BinarySearchTree as bst

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#initialize the BST
search_names1 = bst(names_1[0])
#loop through all the elements in the file
for i in range(1, len(names_1)):
    #insert each element into the BST
    search_names1.insert(names_1[i])

#loop through the second list from file 2
for duplicate_names in names_2:
    #if there are any duplicates
    if search_names1.contains(duplicate_names):
        #add it to our list
        duplicates.append(duplicate_names) 

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
