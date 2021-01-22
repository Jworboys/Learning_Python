
''' These lines could be minimized by casting as the input is recived.'''
user_age = input("Enter your age: ")
years = int(user_age)
months = years * 12
print(f"Your age, {years}, is equal to {months} months.")

''' Better form for the same representation'''
user_age = int(input("Enter your age: "))
months = user_age  * 12
print(f"Your age, {user_age}, is equal to {months} months.")