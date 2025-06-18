calc_num1 = float(input("Enter number 1 "))
calc_num2 = float(input("Enter number 2 "))
operation = input("Enter the opration to be done ")
if operation == "addition":
    print(calc_num1+calc_num2)
elif operation == "substraction":
    print(calc_num1-calc_num2)
elif operation == "multiplication":
    print(calc_num1*calc_num2)
else :
    print(calc_num1/calc_num2)