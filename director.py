from jumper import Jumper
from words import Words
from letter import Letter

class Director:

    def __init__(self):
        self.player_guess = None
        self._is_playing = True
        self._jumper = Jumper()
        self._word = Words.getRandom()
        print(self._word)
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
        Letter.update_letters(self.player_guess, self._letters)
        Director.update_Jumper(self.player_guess, self._letters, self._jumper)
        
    def update_Jumper(guess, letters, jumper):
        if not Letter.is_correct(guess, letters):
            jumper.cut_line()

    def do_outputs(self):
        #create dashes for blank word
        print(Letter.draw_letters(self._letters))
        # draw jumper dude
        self._jumper.draw()
        # replace dash with letter if guess is correct
        if self._jumper.is_dead():
            self._is_playing = False
        if self.has_won():
            self._is_playing = False
            print("Congratulations!")
    
    def has_won(self):
        has_won = True
        
        for letter in self._letters:
            if letter.guessed == False:
                has_won = False
        
        return has_won


        
letters = Director.make_letters("banjo")
Letter.update_letters("a", letters)




