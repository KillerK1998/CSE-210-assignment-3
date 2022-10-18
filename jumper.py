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




def __init__(self):
    self.lines = 4
def __cut_line(self):
    pass
def draw(self):
    print(PARACHUTE_STATES(self.lines))