'''Obataninig user input to save into a name'''
name = input("Enter your name: ")
print(name)

''' The input function always gives back a STRING
remeber this as if your trying to obtain an interger from the user'''
size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"{square_feet} square feet is {square_meters:.2f} square meters.")