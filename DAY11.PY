# write a program to enter a number and display its and its hex and octal equavalent and its square root.
num = int(input("enter a number : "))
print ("Hexadecimal of " + str(num) + " : " + str(hex(num)))
print ("Octal of " + str(num) + "  : " + str(oct(num)))
print("Square root of " + str(num) + " : " + str(num**0.5))