print ("Python Intro assignment")

Num1 = float(input("Enter first number: "))
Num2 = float(input("Enter second number: "))
operator = input("Enter the operator (+,-, *, /): ")

if operator == "+": 
    print(Num1, "+" , Num2, "=", Num1 + Num2) 

elif operator == "-": 
    print(Num1, "-" , Num2, "=", Num1 - Num2) 

elif operator == "*": 
    print(Num1, "*" , Num2, "=", Num1 * Num2) 

elif operator == "/": 
    print(Num1, "/" , Num2, "=", Num1 / Num2) 

else:
    print("Invalid input")





