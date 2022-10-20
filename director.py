from director import director
from jumper import jumper
from words import words
from letter import letter

class Director:

    def __init__(self):

        self._player_guess = ""
        self._is_playing = True
        self._jumper = jumper()
        self._word = words()
        self.letter = letter()

    def start_game(self):

        while self._is_playing:
            self.getUserGuess()
            self.do_updates()
            self.do_outputs()

    def getUserGuess():
        user_guess = input("Guess a letter [a-z]: ")
        return user_guess

    def do_updates(self):
        pass

    def do_outputs(self):
        pass
    def win_condition():
        #if self.user_guess == jumper_word
        pass
        



