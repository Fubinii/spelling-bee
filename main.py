from spelling_beer import SpellingBeerGame
from extra_code import load_words

default_words = 'SB_en_US.txt'
words = load_words(default_words)
game = SpellingBeerGame(words)


while True: # Start of the game

    print("SPELLING BEE(R)")
    print("------------")
    print("Current word list:", default_words, "To change, type !wordlist <filename>")

    # Initialization of a round
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
            
    # Game Loop
    game.play()

    print("New game? (y/n)")
    if input().lower() != 'y':
        break

