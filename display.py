import math

def display_letters(letters, center_letter, score, current_rank, show_score=True, show_ranks=True):
    letters = letters.replace(center_letter, '')
    # Honeycomb display for 7 letters
    if len(letters)+1 == 7:
        letters = letters[:3] + center_letter + letters[3:]
        print(' ', letters[0].upper(), letters[1].upper(), '  |', end=' ')
        if show_ranks:
            print(f'Score:  {score}')
            
        else:
            print()
        print(letters[2].upper(), '('+letters[3].upper()+')', letters[4].upper(), '|', end=' ')
        if show_score: 
            print(f'Rank:   {current_rank}') 
        else:
            print()
        print(' ', letters[5].upper(), letters[6].upper(), '  |')
    
    else:
        letters = center_letter + letters
        n = math.ceil(math.sqrt(len(letters)))
        for i, letter in enumerate(letters):
            if i%n == 0 and i != 0: 
                print()
                print('', end=' ')
            if letter != center_letter:
                print(letter.upper(), end=" ")
            else: 
                print('(' + letter.upper() + ')', end="")
            
        print()
        print(f'Score: {score}, Rank: {current_rank}') 
        return None