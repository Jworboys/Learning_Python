
#Step 1
name = "Bob"
'''f String'''
greeting = f"Hello, {name}"
print(greeting)

#Step 2
name = "Rolf"
'''Note gretting still contains Bob, as it was assaigned prior to name 
    being changed to Rolf; it doesnt change dynmaically'''
print(greeting)

#Step 3
'''But if you print it dynamically then it will work'''
print(f"Hello, {name}")


#Step 4
name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

'''This can now be used dynamically or static, by changing the variable
    that is passed into the the formated greeting ---- Gretting is now a template'''
with_name_two = greeting.format("Rolf")
print(with_name_two)

'''Formatted Strings or templates can also contain multiple variables'''
longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)
