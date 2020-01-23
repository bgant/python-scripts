# Caesar Cipher Hacker (brute force)
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

# Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.' # Capitalization denotes variable is Constant

# The string to be encrypted/decrypted
message = input('Enter ciphertext: ')

# Store the encrypted/decrypted form of the message
translated = ''

# Loop through every possible key
for key in range(len(SYMBOLS)):
    # It is important to set translated to a blank string each iteration
    translated = ''

    # The rest of the program is almost the same as caesarCipher.py
    for symbol in message:
        # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle wraparound if needed
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbol missing from SYMBOLS without encrypting/decrypting
            translated = translated + symbol

    # Print every possible decryption
    print('Key #%s:  %s' % (key, translated))
