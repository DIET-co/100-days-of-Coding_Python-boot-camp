print("Welcome to the rollercoaster:")

height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age"))
    if age <= 12:
        print("please pay $5.")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12")
else:
    print("Sorry you have to grow taller")          

weight = 85
height = 1.85
 
bmi = weight / (height ** 2)
 
if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")         