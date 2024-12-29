print("Welcome to the rollercoaster:")

height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age"))
    if age <= 12:
        bill = 5
        print("please pay $5.")
    elif age <= 18:
        bill = 7
        print("please pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything will okay")    
    else:
        bill = 12
        print("please pay $12")

    wants_photo = input("do you want to have a photo taken? y for YES and n for NO \n")         

    if wants_photo == 'y':
        bill += 7

    print(f"Your final bill is {bill}")

else:
    print("Sorry you have to grow taller")


