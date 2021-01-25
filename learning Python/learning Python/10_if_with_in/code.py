movies_watched = {"The Matrix", "Green book", "Her"}
user_movie = input("Enter something you have watched recently: ")

if user_movie in movies_watched:
    print(f"I've watcherd {user_movie} too!")
else:
    print("I have not watched that yet.")



number = 7
user_input = input("Eneter 'y' if you would like to play: ").lower()

if user_input == 'y':
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs (number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry you guessed wrong!")