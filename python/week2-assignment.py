
# 1. Create an empty list called my_list. 
my_list = []





# 2. Append the following elements to my_list: 10, 20, 30, 40. 
my_list = []  # Creating an empty list

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)  # Output: [10, 20, 30, 40]




# 3. Insert the value 15 at the second position in the list. 
my_list = [10, 20, 30, 40]  # Existing list

my_list.insert(1, 15)  # Insert 15 at index 1

print(my_list)  # Output: [10, 15, 20, 30, 40]






# 4. Extend my_list with another list: [50, 60, 70].
my_list = [10, 15, 20, 30, 40]  # Existing list

my_list.extend([50, 60, 70])  # Extending with another list

print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60, 70]








# 5. Remove the last element from my_list. 
my_list = [10, 15, 20, 30, 40, 50, 60, 70]  # Existing list

my_list.pop()  # Removes the last element

print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]
# Alternatively, you can use slicing to remove the last element:

my_list = my_list[:-1]

print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]









# 6. Sort my_list in ascending order. 
my_list = [10, 15, 20, 30, 40, 50, 60]  # Existing list

my_list.sort()  # Sorts in ascending order

print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

# Alternatively, you can use the sorted() function if you want to keep the original list unchanged:

sorted_list = sorted(my_list)

print(sorted_list)  # Output: [10, 15, 20, 30, 40, 50, 60] 










# 7. Find and print the index of the value 30 in my_list.
my_list = [10, 15, 20, 30, 40, 50, 60]  # Existing list

index_of_30 = my_list.index(30)  # Find index of 30

print(index_of_30)  # Output: 3




