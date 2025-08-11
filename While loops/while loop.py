#practice while loop

x = 0
y = 5
while x < 13:
    x += 1  # Increment x by 1 in each iteration
    if x == 5:
        continue # Skip the rest of the loop when x is 5
    if x == 10:
        break # Exit the loop when x is 10

    print(x)  # Print the value of x



