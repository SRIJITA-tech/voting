# minicalculator
# 1.add
# 2.subtraction
# 3.multiplication
# 4.division

print("Select an operation to perform:")
print("1.add")
print("2.subtraction")
print("3.multiplication")
print("4.division")

operation = input()
if operation == "1":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("the sum is " + str(int(num1)+int(num2)))
elif operation == "2":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("the difference is"+ str(int(num1)-int(num2)))
elif operation == "3":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("the product is"+ str(int(num1)*int(num2)))
elif operation == "4":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("the result is" + str(int(num1)/int(num2)))
else:
    print("invalid entry")



