''' Return and everything work the same 
    as other languages'''

def add (x,y):
    print(x + y)
    return x + y

add(5, 8)
result = add (5, 8)
print (result)


def divide(dividend, divisor):
    if divisor != 0: 
        return dividend / divisor
    else:
        return "You fool!"

result = divide(15,2)
print(result)