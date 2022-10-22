
class Letter:
    def __init__(self):
        self.char = ""
        self.guessed = False

    def getUserGuess():
        user_guess = input("Guess a letter [a-z]: ")
        return user_guess
    
    def make_letter_line(letters):
        letter_line = ""
        for letter in letters:
            if letter.guessed == True:
                letter_line += letter.char
            else:
                letter_line += "_"
            letter_line += " "
        return letter_line

    def draw_letters(letters):
        letter_line = Letter.make_letter_line(letters)
        print(letter_line)

    def update_letters(char, letters):
        for letter in letters:
            if letter.char == char:
                letter.guessed = True

    def is_correct(char, letters):
        is_correct = False

        for letter in letters:
            if letter.char == char:
                is_correct = True

        return is_correct
   


