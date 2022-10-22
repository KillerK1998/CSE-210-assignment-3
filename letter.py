
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

    def update_letters():
        player_guess = Letter.getUserGuess()
        word_length = Letter.draw_letters()

        


   


