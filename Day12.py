# write a program to calculate area of triangle using Heron's formula
# HINT: Heron's formula  => area = sqrt(S*(S-a)*(S-b)*(S-c)))
a = float(input("Enter the first side of the triangle : "))
b = float(input("Enter the secound side of the triangle : "))
c = float(input("Enter the third side of the triangle : "))
print(a,b,c)
area = (S*(S-a)*(S-b)*(S-c))**0.5
print("Area = " + str(area))