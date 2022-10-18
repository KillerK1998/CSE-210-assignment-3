from words import words

class letter:
    user_guess = input("Guess a letter [a-z]: ")

    if user_guess == words:
        print(user_guess)
    else:
        print("_")


