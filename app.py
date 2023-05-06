import itertools
import time

password = input("Enter the passowrd for this device: ")

# We need to set the range of numbers to loop to an from. must be 4-digit
looper = itertools.product(range(10), repeat=6)

# Timer Should start here
timeframe = time.time()

# Now that has been setup. We need to loop through to get the saved password while checking against the saved password itself
for loops in looper:
    password_cracker = "".join(str(digit) for digit in loops)

    if password_cracker == password:
        print("Cracked my boy. The password is: ", password_cracker)
        break

else:
    print("Password in a higher range of numbers.")
    

timeLength = time.time() - timeframe
print("It took ", timeLength, " to calculate")