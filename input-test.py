#this module is used to test the input function

#collect input
lb = int(input("Enter lower bound: "))
ub = int(input("Enter upper bound: "))

#print statement and collect additional input
print("\nYou chose {0} as your lower bound, \
and {1} as your upper bound.".format(lb, ub))
verif = input("\nProceed? (y/n): ")
response = verif.lower()

#run the multiplication table if the user confirms
if response == 'y':
    for multiplier in range(lb, ub + 1):
        for i in range(1, 12):
            print(i, "x", multiplier, "=", i * multiplier)
else:
    print("We're done!")




#code below is for reference only, not executed
#if response == 'y':
#        for i in range(1, 11):
#            print(f"{multiplier} times {i} is {multiplier * i}")
#        print(f"{multiplier} times 2 is {multiplier * 2}")