#another practice file for loops

#for i in range(1, 20):
#    print(i)
#    with open("numbers.txt", "w") as f:
#        f.write(str(i) + '\n')

#with open("numbers.txt", "w") as f:
#    for i in range(1, 20):
#        f.write(str(i) + '\n')
#       print(i, end=' ')


#f = open("numbers.txt")
#for line in f:
#    print(line.strip())  # Use strip() to remove any trailing newline characters

i = [(5, 6), 123, 'abc', 'hello', 456, 'world']
query = [(5, 6), (7, 8), (9, 10)]
for key in query:
    if key in i:
        print(f"Found {key} in list")

    else:
        print(f"{key} not found in list")

