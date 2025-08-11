#dataset examples


my_list = ['time', 'SPACE', 'Matter', 'energy']
t = [] #this is an empty list
for i in my_list:
    if i.islower():  # Check if the string is in lowercase
        t.append(i)  # Append to the new list if it is lowercase
my_list = t
print(my_list)  # Output the modified list containing only lowercase strings



