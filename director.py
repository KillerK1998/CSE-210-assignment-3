from director import director
from jumper import jumper
from words import words

class Director:

    def __init__(self):

        self._player_guess = ""
        self._is_playing = True
        self._jumper = Jumper()
        self._word = Words()

    def start_game(self):

        while self._is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        pass

    def do_updates(self):
        pass

    def do_outputs(self):
        pass
    


