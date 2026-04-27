from pathlib import Path
from spelling_beer import SpellingBeerGame
from extra_code import load_words

BASE_DIR = Path(__file__).parent
WORDLIST = BASE_DIR / "wordlists" / "SB_en_US.txt"

def main():
    default_wordlist = WORDLIST
    words = load_words(default_wordlist)
    game = SpellingBeerGame(words)

    while True: # Start of the game

        print("SPELLING BEE(R)")
        print("------------")
        print("Current word list:", default_wordlist) 
        print("To change to a different list from the \"wordlists\" folder, type !wordlist <filename> .")

        # Initialization of a round
        while True:
            first_input = input("Type in letters to initialize game or use !generate: ").lower()

            if first_input.startswith("!wordlist "):
                filename = first_input.split(" ", 1)[1].strip()
                candidate = BASE_DIR / "wordlists" / filename
                if candidate.exists() and candidate.is_file():
                    try:
                        words = load_words(candidate)
                        default_wordlist = candidate
                        print("Word list change successful! Using:", default_wordlist)
                    except FileNotFoundError:
                        print("Unable to open file. Using default word list.")
                else:
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


if __name__ == "__main__":
    main()

