# Vigenere Cipher (Polyalphabetic Substitution/Caesar Cipher)
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = """
Alan Mathison Turing was a British mathematician,
logician, cryptanalyst, and computer scientist.
"""

    myKey = 'Asimov'

    myMode = 'encrypt'  # Set to either 'encrypt' or 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    print()


def encryptMessage(key, message):
    return translatedMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translatedMessage(key, message, 'decrypt')

def translatedMessage(key, message, mode):
    translated = []  # Stores the encrypted/decrypted message string

    keyIndex = 0  # Start with the first letter of the key which is key[0]
    key = key.upper()  # Make sure the key is all upper case letters before using

    for symbol in message:  # Loop through each symbol in message
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])  # Add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])  # Subtract if decrypting

            num %= len(LETTERS)  # Handle any wraparound of letters either positive or negative

            # Add the encrypted/decrypted symbol to the end of translated string
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1  # Move to the next letter in the key
            #if keyIndex == len(key):  # Handle wraparound of key
            #    keyIndex = 0
            keyIndex %= len(key)  # Handle wraparound of key similar to num %= len(LETTERS) above

        else:
            # Append the symbol without encrypting/decrypting
            translated.append(symbol)

    return ''.join(translated)


# If vigenereCipher.py is run (instead of imported as a module), call the main() function
if __name__ == '__main__':
    main()

