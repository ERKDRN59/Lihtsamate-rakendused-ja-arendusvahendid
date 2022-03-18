print("Calculator")
print("Made by Erik Jurgenson (IT-21V)")
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
act = input("What do you want to do with those numbers? (+, -, *, /): ")
if(act == "+"):
    print("You selected summing")
    eq = a+b
    print(a, act, b, "=", eq)
elif(act == "-"):
    print("You selected substracting")
    eq = a-b
    print(a, act, b, "=", eq)
elif(act == "*"):
    print("You selected multiplying")
    eq = a*b
    print(a, act, b, "=", eq)
else:
    print("You selected dividing")
    eq = a/b
    print(a, act, b, "=", eq)
