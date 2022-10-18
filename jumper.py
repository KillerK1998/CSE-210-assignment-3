#cutLine()--Responsible for storing the state of the Jumper (how many lines have been removed
# from parachute), draw()--prints Jumper on the command line

PARACHUTE_STATES = [
    """
      x
     /|\\
     / \\""",
    """
     \\ /
      O
     /|\\
     / \\""",
    """
    \\   /
     \\ /
      O
     /|\\
     / \\""",
    """
    /___\\
    \\   /
     \\ /
      O
     /|\\
     / \\""",
    """
     ___ 
    /___\\
    \\   /
     \\ /
      O
     /|\\
     / \\"""
]



class Jumper:
    def __init__(self):
        self.lines = 4
    def cut_line(self):
        self.lines = self.lines - 1
    def draw(self):
        print(PARACHUTE_STATES(self.lines))