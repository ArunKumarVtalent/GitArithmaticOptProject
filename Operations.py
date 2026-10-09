from Sample import Sample

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))


obj = Sample()
print("Addition of two numbers is: ", obj.Add(a, b))
print("Subtraction of two numbers is: ", obj.Subtract(a, b))
print("Multiplication of two numbers is: ", obj.Multiply(a, b))

print("Program executed successfully")

