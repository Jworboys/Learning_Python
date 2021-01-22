friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob" , "Anne"}

''' Finding the  diffrence between friends and abroad'''
''' If you did the opposite such as abroad.diffrence(friends) nothing 
    would return, you would have an empty set. This set would be empty
    because bob and Anne are already bot in friends. Leaving abroad to
    have nothing. The print will print set() indicating an empty set'''

local_friends = friends.difference(abroad)
print(local_friends)



local = {"Rolf", "Bob"}
abroad_num2 = {"Bob", "Anne"}

''' Combines the diffrences into one, same as a uninon in stats ''' 
friends2 = local.union(abroad_num2)
print(friends2)


art = {"Bob" , "Jen" , "Rolf", "Charlie"}
science = {"Bob" , "Jen", "Adam", "Anne"}

''' Intersection shows the middle area of a vinn diagram '''
both = art.intersection(science)
print(both)
