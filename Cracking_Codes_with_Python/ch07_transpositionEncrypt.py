# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

def main():
    #myMessage = 'Common sense is not so common.'
    myMessage = input('plaintext: ')
    #myKey = 8
    myKey = int(input('key [0 to %s]: ' % int(len(myMessage)/2)))

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at 
    # the end of the encrypted message.
    print(ciphertext + '|')

def encryptMessage(key, message):
    # Each string in the ciphertext represents a column in the grid
    ciphertext = [''] * key

    # Loop through each column in ciphertext
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it
    return ''.join(ciphertext)

# If transpositionEncryt.py is run (instead of imported as a module) call
# the main() function
if __name__ == '__main__':
    main()

