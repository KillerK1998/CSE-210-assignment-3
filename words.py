# Python code to pick a random
# word from a text file
import random
  
# Open the file in read mode
with open("words.txt", "r") as file:
    allText = file.read()
    words = allText.split()
  
    # print random string
    print(random.choice(words))