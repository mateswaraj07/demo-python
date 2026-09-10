# writeto convert minutes into minutes into hours and print it
# example 135 is 2 hours and 15 minutes
minutes = int(input("Enter minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} is {hours} hours and {remaining_minutes} minutes")