

# boolean logic examples

fmenu = {'spam': 1.50, 'ham': 1.99, 'eggs': 0.99}
corder = input("What would you like today--spam, ham or eggs?): ")

if corder == 'spam':
    print("For the spam, that will be", "$", "%.2f" % fmenu.get('spam'), "please")
elif corder == 'ham':
    print("For the ham, that will be", "$", "%.2f" % fmenu.get('ham'), "please")
else:
    print("Eggs by default! Your total is", "$", "%.2f" % fmenu.get('eggs'))


#code below are different examples of string formatting
#formatted_number = f"{number:.2f}"
#formatted_number = "{:.2f}".format(number)