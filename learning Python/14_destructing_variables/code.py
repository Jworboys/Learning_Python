''' The brackets for x = (5,11) are not always needed''' 
t = 5, 11
x, y = t

'''Python knows that because we are assigning to values to a tuple
    each value being assigned will get one of the tuple's'''
print(x , y)


people = [("Bob", 96, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")


''' using _ just as a name indicates that it will not be used'''
person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)

''' Head will be 1 *tail will collect all the others'''
head,*tail = [1,2,3,4,5]
print(head)
print(tail)

''' Here the head will contain all besides the last one'''
*head, tail = [1,2,3,4,5]
print(head)
print(tail)