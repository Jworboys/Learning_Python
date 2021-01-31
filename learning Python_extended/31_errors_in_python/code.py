'''ZeroDivisionError is an execption error hhandler like c#'''

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor  


grades = []

print("Welcome to the average grade program")

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades in your list yet.")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you!")

''' Try except same as try catch ''' 