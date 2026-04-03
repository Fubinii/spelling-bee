import random
import math
from collections import Counter
from time import sleep
from extra_code import create_wordlist, provide_start, word_score
from display import display_letters

# c_letter:     center letter
# o_letters:    outer letters (without the center letter)
# letters:      all letters

class SpellingBeerGame:
    def __init__(self, words):
        self.words = words
        self.o_letters = None
        self.c_letter = None
        self.valid_words = set()
        self.found_words = set()
        self.history = []
        self.pangrams = set()
        self.total_score = 0
        self.score = 0
        self.ranks = []
        self.current_rank = 'Beginner'

        self.commands = {
            "!help": self.command_help,
            "!exit": self.command_exit,
            "!found": self.command_found,
            "!hints": self.command_hints,
            "!f2": self.command_ft,
            "!f2l": self.command_ftl,
            "!pangrams": self.command_pangrams,
            "!ranks": self.command_ranks,
            "!reveal": self.command_reveal,
            "!end": self.command_reveal,
            "!shuffle": self.command_shuffle
    }


    def __str__(self):
        return f"SpellingBeerGame(center={self.c_letter}, outer={self.o_letters})"

    # === Small Helper Methods ===
    def feedback(self, word):
        if word in self.pangrams:
            print("*** PANGRAM! ***")
        elif len(word) < 5: 
            print("Good!")
        elif len(word) < 7:
            print("Splendid!")
        elif len(word) < 9:
            print("Excellent!")
        else:
            print(f"A {len(word)}-letter word, Marvelous!")
    
    # === Commands ===
    def command_help(self):
        print("!exit - Exit current game")
        print("!found - Show already found words")
        print("!hints - Show available hint commands")
        print("!pangrams - Show how many pangrams there are")
        print("!ranks - Show the points needed for each rank")
        print("!reveal, !end - Reveal all valid words (ends the game)")
        print("!shuffle - Shuffle the letters")

    def command_exit(self):
        return 'break'
    
    def command_found(self):
        print("Found words:")
        for word in sorted(self.found_words):
            if word in self.pangrams:
                print(word.upper(), end=", ")
            else:
                print(word, end=", ")
        print()
        return None
    
    # --- Hints ---
    def command_hints(self):
        print("!pangrams - Show how many pangrams there are.")
        print("!f2 - List of first two letters of all valid words.")
        print("!f2l - List of first two letters and length of each valid words.")
        return None
    
    def command_pangrams(self):
        print(f"There are {len(self.pangrams)} possible pangrams with these letters.")
        return None
    
    def command_ft(self):
        ft_counter = Counter()
        for word in self.valid_words:
            first_two = word[:2].upper()
            ft_counter[first_two] += 1

        # # Still have to decide what look nicer, this
        # for entry, count in sorted(ft_counter.items()):
        #     print(f"{entry}-{count}")

        # Or this
        results = [f"{entry}-{count}" for entry, count in sorted(ft_counter.items())]
        print(", ".join(results))
        return None   

    def command_ftl(self):
        results = [f"{word[:2].upper()}({len(word)})" for word in sorted(self.valid_words)]
        print(", ".join(results))
        return None
    # ---

    def command_ranks(self):
        for t, r in self.ranks:
            print(f"{r}: {t} points")
        return None
    
    def command_reveal(self):
        print(f"Revealed at {self.score} / {self.total_score} points. Valid words were:")
        for word in sorted(self.valid_words):
            if word in self.found_words and word in self.pangrams:
                print('✓ ', word.upper())
            elif word in self.found_words:
                print('✓ ', word)
            elif word in self.pangrams:
                print(word.upper())
            else:
                print(word)
        return 'break'
    
    def command_shuffle(self):
        l = list(self.o_letters)
        random.shuffle(l)
        self.o_letters = ''.join(l)

    
    # === Initialization of the Game ===
    def determine_score(self):
        self.total_score = sum(word_score(word, self.pangrams) for word in self.valid_words)
    
    def determine_ranks(self):
        self.ranks = [
            (math.floor(0.05*self.total_score), 'Moving Up'),
            (math.floor(0.08*self.total_score), 'Good'),
            (math.floor(0.15*self.total_score), 'Solid'),
            (math.floor(0.25*self.total_score), 'Nice'),
            (math.floor(0.4*self.total_score), 'Great'),
            (math.floor(0.5*self.total_score), 'Amazing'),
            (math.floor(0.7*self.total_score), 'Genius'),
            (self.total_score, 'Queen Bee')
        ]

    def from_generate(self):
        self.o_letters, self.c_letter, self.valid_words, self.pangrams = provide_start(self.words)

    def from_input(self, first_input):
        letters = ''.join(dict.fromkeys(first_input))

        print('Available letters:', end=' ')
        for letter in letters:
            print(letter.upper(), end=' ')
        print()
        print("Chose a center letter:") 

        center_invalid = True
        while center_invalid:
            self.c_letter = input().lower()
            if self.c_letter not in letters:
                print("Center letter must be one of the letters you initialized.")
            else:
                center_invalid = False
        
        self.o_letters = letters.replace(self.c_letter, '')

        self.valid_words, self.pangrams = create_wordlist(self.o_letters, self.c_letter, self.words)

    #=== Active Game ===
    def play(self):
        self.determine_score()
        self.determine_ranks()
        self.o_letters, self.c_letter = self.o_letters.upper(), self.c_letter.upper()

        print(f'Maximum score: {self.total_score} points. Pangrams: {len(self.pangrams)}')
        display_letters(self.o_letters, self.c_letter, 0, self.current_rank)
        print('Start by typing a word. (For a list of commands type !help)')
        while True:
            user_input = input().lower()

            if user_input in self.commands:
                result = self.commands[user_input]()
                if result == 'break':
                    break

            elif user_input in self.valid_words and user_input not in self.found_words:
                self.found_words.add(user_input)
                self.history.append(user_input)
                if len(self.history) > 4: self.history.pop(0)
                self.score += word_score(user_input, self.pangrams)

                self.feedback(user_input)

                # Rank update    
                self.current_rank = next((r for t, r in reversed(self.ranks) if self.score >= t), 'Beginner')

            elif user_input in self.found_words:
                print("Already found.")
            else:
                print("Not in word list.")          
            sleep(0.5)
            print()
            print("Last: ", end="")  
            print(", ".join(reversed(self.history)))
            display_letters(self.o_letters, self.c_letter, self.score, self.current_rank)
            
    
