num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
opr=input("Enter operator (+, -, *, /): ")
if opr=='+':
    result=num1+num2
    print("The result is:", result)
elif opr=='-':
    result=num1-num2
    print("The result is:", result)
elif opr=='*':
    result=num1*num2
    print("The result is:", result)
elif opr=='/':
    result=num1/num2
    print("The result is:", result)
else:
    print("Invalid operator") 
print(num1, opr, num2, "=", result)