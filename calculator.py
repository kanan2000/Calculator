print("Select an order of operation from 1-4")
print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")

operation = input()

if operation == "1":
    num1 = input("What is your first number:")
    num2 = input("What is your second number:")
    print("The sum is " + str(int(num1) + int(num2)))

elif operation == "2":
    num1 = input("What is your first number:")
    num2 = input("What is your second number:")
    print("the sum is " + str(int(num1)- int(num2)))

elif operation == "3":
    num1 = input("What is your first number:")
    num2 = input("What is your second number:")
    print("the sum is " + str(int(num1)* int(num2)))

elif operation == "4":
    num1 = input("What is your first number:")
    num2 = input("What is your second number:")
    print("the sum is " + str(int(num1)/ int(num2)))