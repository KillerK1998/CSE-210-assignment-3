from director import Director
from words import Words
import pytest

def test_make_letters():
    word = "banjo"

    letters = Director.make_letters(word)
    length = len(word)

    for i in range(length):
        assert word[i] == letters[i].char

def test_make_letter_line():
    word = "banjo"

    letters = Director.make_letters(word)
    letters_line = Director.make_letter_line(letters)

    assert letters_line == "_ _ _ _ _ "

    word = "banjo"
    letters = Director.make_letters(word)
    letters[0].guessed = True
    letters[2].guessed = True
    letters[4].guessed = True
    letters_line = Director.make_letter_line(letters)

    assert letters_line == "b _ n _ o "

pytest.main(["-v", "--tb=line", "-rN", __file__])