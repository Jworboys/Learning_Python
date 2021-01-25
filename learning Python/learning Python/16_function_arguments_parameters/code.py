'''Arugments are the same as other languages'''
def add(x,y):
    result = x + y
    print(result)

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")




add(5,3)

'''Parameters can be the same as a normal language or
    they can be assigned the value; so they can be nonorded.'''

say_hello(surname = "Bob", name = "Smith")

''' Just makes everything more readable'''
''' If you dont use full keyword arguments the 
    postion arguments must go first'''
divide(dividend = 15, divisor = 0)