
# another if statement example


yn = input("Do you want to continue? Yes or No: ")
yn = yn.lower()

if yn[0] == 'y':
    print("You typed 'yes'")
elif yn[0] == 'n':
    print("You typed 'no'")
elif yn == 'spam':
    print("What are you doing?!")
else:
    print("You entered an invalid response")
