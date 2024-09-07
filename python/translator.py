import sys

# Braille Alphabet Mapping
braille_alphabet = {
    'a': '.....',
    'b': '....O',
    'c': '....OO',
    'd': '...O..',
    'e': '...O.O',
    'f': '...OO.',
    'g': '...OOO',
    'h': '..O...',
    'i': '..O..O',
    'j': '..O.OO',
    'k': '..OO..',
    'l': '..OO.O',
    'm': '..OOOO',
    'n': '.O....',
    'o': '.O...O',
    'p': '.O..O.',
    'q': '.O..OO',
    'r': '.O.O..',
    's': '.O.O.O',
    't': '.O.OOO',
    'u': '.OO...',
    'v': '.OO..O',
    'w': '.OO.O.',
    'x': '.OO.OO',
    'y': '.OOO..',
    'z': '.OOO.O',
    ' ': '......',
    ',': '..O...',
    '.': '.....O',
    '?': '..O.OO',
    '!': '..OO.O',
    "'": '..OOO.',
    '-': '.O....',
    '/': '.O.O..',
    '(': '.O.OO.',
    ')': '.OO...',
    ':': '.OO.O.',
    ';': '.OO.OO',
    '_': '.OOO..',
    '"': '.OOO.O',
    '#': '.OOOO.',
    '*': '.OOOOO',
    '0': '.O.OOOO',
    '1': '.OO....',
    '2': '.OO...O',
    '3': '.OO..O.',
    '4': '.OO..OO',
    '5': '.OO.O..',
    '6': '.OO.O.O',
    '7': '.OO.OOO',
    '8': '.OOO...',
    '9': '.OOO..O',
    'capital': '..O....',
    'number': '.O.OO..'
}

# Inverse Braille Alphabet Mapping
inverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}

def to_braille(text):
    braille_text = ''
    capitalize_next = False
    is_number = False

    for char in text:
        if char.isupper():
            braille_text += braille_alphabet['capital']
            char = char.lower()
        elif char.isdigit():
            if not is_number:
                braille_text += braille_alphabet['number']
                is_number = True
        else:
            is_number = False

        braille_text += braille_alphabet[char]

    return braille_text

def to_english(braille_text):
    english_text = ''
    capitalize_next = False
    is_number = False

    i = 0
    while i < len(braille_text):
        char = braille_text[i:i+6]
        if char == braille_alphabet['capital']:
            capitalize_next = True
            i += 6
            continue
        elif char == braille_alphabet['number']:
            is_number = True
            i += 6
            continue
        elif char == braille_alphabet[' ']:
            is_number = False
            capitalize_next = False

        if is_number:
            english_text += inverse_braille_alphabet[char]
        elif capitalize_next:
            english_text += inverse_braille_alphabet[char].upper()
            capitalize_next = False
        else:
            english_text += inverse_braille_alphabet[char]

        i += 6

    return english_text

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    text = sys.argv[1]

    if text.startswith('.....') or text.startswith('....O') or text.startswith('....OO'):
        print(to_english(text))
    else:
        print(to_braille(text))

if __name__ == "__main__":
    main()
