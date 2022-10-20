# Python code to pick a random
# word from a text file
import random
  
# Open the file in read mode
class Words:
    def getRandom():
        with open("list.txt", "r") as file:
            allText = file.read()
            words = allText.split()
        
            return random.choice(words)