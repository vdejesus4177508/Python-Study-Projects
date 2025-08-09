#more boolean logic examples


while True: #run risk of infinite loop
    s = input("Enter a string of at least 4 characters, or 'q' to quit: ")
    if s.lower() == 'q':
        print("You entered 'q'. Exiting the program.")
        break  # Exit the loop if the user enters 'q'

    elif len(s) < 4:
        print("The string is too short. Please enter at least 4 characters.")
        continue #Continue to the next iteration if the string is too short


    raise SystemExit("Exiting the program due to an error in the input string.")


