from jumper import Jumper
from words import Words
from letter import Letter

class Director:

    def __init__(self):
        self.player_guess = None
        self._is_playing = True
        self._jumper = Jumper()
        self._word = Words.getRandom()
        self._letters = Director.make_letters(self._word)

    def make_letters(word):
        letters = []
        for char in word:
            letter = Letter()
            letter.char = char
            letters.append(letter)
        return letters

    def start_game(self):

        while self._is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        self.player_guess = Letter.getUserGuess()

    def do_updates(self):
        # if player guess is the same as the letter, the guess is true, else it is false
        # and the cut line function gets called
        if self.player_guess == self.letters:
            self.player_guess = True
        else:
            self.player_guess = False
            Jumper.cut_line()


    def do_outputs(self, letters):
        #create dashes for blank word
        for i in len(self.letters()):
            print('- ')
        # draw jumper dude
        Jumper.draw()
        # replace dash with letter if guess is correct
        for i in len(self.letters()):
            if self.player_guess == i:
                letters.append(i)

    def draw_letters(letters):
        letter_line = Director.make_letter_line(letters)
        print(letter_line)

    def make_letter_line(letters):
        letter_line = ""
        for letter in letters:
            if letter.guessed == True:
                letter_line += letter.char
            else:
                letter_line += "_"
            letter_line += " "
        return letter_line


        





