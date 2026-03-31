import random
import math
from time import sleep
from spelling_beer import SpellingBeerGame
from extra_code import load_words, create_wordlist, provide_start, word_score
from display import display_letters

default_words = 'en_US_60_SB.txt'
words = load_words(default_words)
game = SpellingBeerGame(words)

print("SPELLING BEE(R)")
print("------------")
print("Current word list:", default_words, "To change, type !wordlist <filename>")

while True:
        first_input = input("Type in letters to initialize game or use !generate: ").lower()
        if first_input.startswith("!wordlist "):
            filename = first_input.split(" ", 1)[1]
            try: 
                words = load_words(filename)
                print("Word list change successful!")
            except FileNotFoundError:
                print("File not found. Using default word list.")
        elif first_input == "!generate":
            game.from_generate()
            break
        else:
            game.from_input(first_input)
            break

while True:
    game.play()

    print("New game? (y/n)")
    if input().lower() != 'y':
        break

