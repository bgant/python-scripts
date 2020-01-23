# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

#import pyperclip.py  # Copies script output to clipboard

# Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.' # Capitalization denotes variable is Constant

# Whether the program encrypts or decrypts
mode = ''
while mode != 'e' and  mode != 'd':
    mode = input('(e)ncrypt or (d)ecrypt? ')

# The encryption/decryption key
key = input('Enter Key [0 to %s]: ' % len(SYMBOLS))
key = int(key)

# The string to be encrypted/decrypted
#message = 'This is my secret message.'
if mode == 'e':
    message = input('Enter plaintext: ')
elif mode == 'd':
    message = input('Enter ciphertext: ')

# Store the encrypted/decrypted form of the message
translated = ''

for symbol in message:
    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption
        if mode == 'e':  # Encrypt message
            translatedIndex = symbolIndex + key
        elif mode == 'd':  # Decrypt message
            translatedIndex = symbolIndex - key

        # Handle wraparound if needed
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

    else:
        # Append the symbol missing from SYMBOLS without encrypting/decrypting
        translated = translated + symbol

# Output the translated string
if mode == 'e':
    print('ciphertext: ', translated)
elif mode == 'd':
    print('plaintext: ', translated)
else:
    print('Error')

#pyperclip.copy(translated) # Copies output to clipboard
