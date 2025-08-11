

# This code demonstrates the use of an if statement to check a condition


num = input("Enter a number: ")
num = int(num)

if num < 0:
    print("The absolute value of", num, "is", -num)
else:
    print("The absolute value of", num, "is", num)

