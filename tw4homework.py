# Get user input
num = int(input("Enter a number: "))

# Call the appropriate function based on input value
if num > 0:

    while num > 0:
        print(num)
        num -= 1
    print("Blastoff!")

elif num < 0:
    
    while num < 0:
        print(num)
        num += 1
    print("Blastoff!")

else:
    print("Blastoff!")