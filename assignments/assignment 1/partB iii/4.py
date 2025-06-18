number1 = input ("Enter number 1 ")
number2 = input ("Enter number 2 ")
number3 = input ("Enter number 3 ")

if number1>number2:
    if number1>number3:
        print(f"{number1} is the greatest")
    else:
        print(f"{number3} is the greatest")
elif number2>number3:
    print(f"{number2} is the greatest")
else : print(f"{number3} is the greatest")