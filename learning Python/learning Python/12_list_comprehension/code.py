numbers = [1.3,5]
doubled = [num * 2 for num in numbers]

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [ friend for friend in friends if friend.startswith("S")]

'''This does the same as the above just expanded.'''

'''for friend in friends
    if friend.startswith("S")
        start_s.append(friend)'''

print(starts_s)
print("friends: ", id(friends), "starts_s:", id(starts_s))