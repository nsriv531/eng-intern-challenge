import sys

# Braille Alphabet Mapping
braille_alphabet = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O..',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O...OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
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
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    'capital': '.....O',
    'number': '.O.OO..'
}

# Inverse Braille Alphabet Mapping
inverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}

def to_braille(text):
    braille_text = ''
    is_number = False

    for char in text:
        if char.isupper():
            braille_text += braille_alphabet['capital']  # Append capital marker
            char = char.lower()  # Convert to lowercase for proper mapping

        if char.isdigit():
            if not is_number:
                braille_text += braille_alphabet['number']
                is_number = True
        else:
            is_number = False

        braille_text += braille_alphabet.get(char, braille_alphabet[' '])  # Default to space if char not found

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

    text = ' '.join(sys.argv[1:])  # Removed .lower() to preserve original case

    # Check if input is already in Braille (starts with capital marker or number marker)
    if text.startswith('.....') or text.startswith('....O') or text.startswith('....OO'):
        print(to_english(text))
    else:
        print(to_braille(text))

if __name__ == "__main__":
    main()
