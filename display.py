import math

'''First all the print functions for each specific letter count. 
_patter_X where X is the number of outer letters (ol), so NOT including
the center letter! Otherwise to save typing:
cl: center letter
s:  score
cr: current rank

Afterwards, all function are combined in a dispatch table in print_letters.
'''

def _pattern_4(ol, cl, s, cr):
    print(f'   {ol[0]}     |  Score:  {s}')
    print(f'{ol[1]} ({cl}) {ol[2]}  |  Rank:   {cr}')
    print(f'   {ol[3]}     |')
    return None

def _pattern_5(ol, cl, s, cr):
    print(f'   {ol[0]}     |  Score:  {s}')
    print(f'{ol[1]} ({cl}) {ol[2]}  |  Rank:   {cr}')
    print(f'  {ol[3]} {ol[4]}    |')
    return None

def _pattern_6(ol, cl, s, cr):
    print(f'  {ol[0]} {ol[1]}    |  Score:  {s}')
    print(f'{ol[2]} ({cl}) {ol[3]}  |  Rank:   {cr}')
    print(f'  {ol[4]} {ol[5]}    |')
    return None

def _pattern_7(ol, cl, s, cr):
    print(f'  {ol[0]} {ol[1]}    |  Score:  {s}')
    print(f'{ol[2]} ({cl}) {ol[3]}  |  Rank:   {cr}')
    print(f' {ol[4]} {ol[5]} {ol[6]}   |')
    return None

def _pattern_8(ol, cl, s, cr):
    print(f'{ol[0]}  {ol[1]}  {ol[2]}  |  Score:  {s}')
    print(f'{ol[3]} ({cl}) {ol[4]}  |  Rank:   {cr}')
    print(f'{ol[5]}  {ol[6]}  {ol[7]}  |')
    return None


PATTERNS = {
    4: _pattern_4,
    5: _pattern_5,
    6: _pattern_6,
    7: _pattern_7,
    8: _pattern_8,
}

def display_letters(o_letters, c_letter, score, current_rank):
    printer = PATTERNS.get(len(o_letters))
    if printer: 
        printer(o_letters, c_letter, score, current_rank)
    
    else:
        letters = c_letter + o_letters
        n = math.ceil(math.sqrt(len(letters)))
        for i, letter in enumerate(letters):
            if i%n == 0 and i != 0: 
                print()
                print('', end=' ')
            if letter != c_letter:
                print(letter.upper(), end=" ")
            else: 
                print('(' + letter.upper() + ')', end="")
            
        print()
        print(f'Score: {score}, Rank: {current_rank}') 
    return None



# display_letters('BCDE', 'A', 10, 'Beginner')