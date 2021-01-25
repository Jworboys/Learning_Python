friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
friend_ages["Bob"] = 20
print(friend_ages["Adam"])

friends = [
    {"name": "Jordan", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Larry", "age": 27}
]

print(friends[1]["name"])



student_attendence = {"Rolf": 96, "Bob": 80, "Anner": 100}

for student in student_attendence:
        print(f"{student}: {student_attendence[student]}")

'''Same thing but better way of doing'''
for student, attendence in student_attendence.items():
        print(f"{student}: {attendence}") 



if "Bob" in student_attendence:
    print(f"Bob: {student_attendence['Bob']}")
else:
    print("Bob is not a student in this class.")
    

''' Adding up all the vlaues in order to obtain an average of the attendece.'''
attendence_values  = student_attendence.values()
print(sum(attendence_values)/ len(attendence_values))                                      