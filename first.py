# write a program to check whether a number is even or odd  without if esle
#example 2 = Number is odd : False
n = int(input("Enter a number: "))
result = n % 2 == 0
print("Number is odd:", not result)