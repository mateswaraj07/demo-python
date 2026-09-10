#write a program to extarct the last digit of an number
# OUTPUT= 1234 : last digit is 4
number = int(input("Enter a number: "))
last_digit = number % 10
print(f"{number} : last digit is {last_digit}")