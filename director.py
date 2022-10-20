from jumper import Jumper
from words import Words
from letter import Letter

class Director:

    def __init__(self):

        self._player_guess = ""
        self._is_playing = True
        self._jumper = Jumper()
        self._word = Words.getRandom()
        self._letters = self.makeLetters(self._word)

    def makeLetters(self, word):
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
        pass

    def do_outputs(self):
        pass



