
''' This is how to take input and make the input all lower case'''

day_of_week = input ("What day of the week is it today? ").lower()
print(day_of_week == "Monday")

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("Happy Tuesday!")
else:
    print("Full speed ahead!")

print("This will always run")