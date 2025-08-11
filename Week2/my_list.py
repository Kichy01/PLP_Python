#1.Create an empty list my_list
my_list = [] 

#2.Add elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#3. Insert at index 1 number 15
my_list.insert(1, 15)

# 4. Extend my_list with multiple elements
my_list.extend ([50, 60, 70])

#5. Remove the last element from my_list
my_list.pop(7)

#6 Sort my_list in ascending order
my_list.sort()

print("The final list is:", my_list)
#7. Find and print the index of the value of 30 in my_list
index_of_30 = my_list.index(30)
print (f"Index of 30: {index_of_30}")

#8. Print the final my_list