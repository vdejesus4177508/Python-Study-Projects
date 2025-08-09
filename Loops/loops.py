# the for loop is the counting loop and used to iterate over a sequence (like a list, tuple, or string)

for letter in "Pythons":
    with open("../letter.txt", "a") as f:
        f.write(letter + ' ')
    print(letter, end=' ')

