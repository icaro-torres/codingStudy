# This code implements a simple Caesar cipher encryption algorithm.
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
# This function just joins the alphabet with itself to enable the "shift" without giving an index error.

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
# This function prompts the user to enter a message to encrypt and returns it.

def getCipherKey():
    shiftAmount = input("Please enter a key (whole numbers from 1 to 25): ")
    return shiftAmount
# Here the user will enter the number that will define how much the letters will be shifted.

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseAlphabet = message.upper()
    for currentCharacter in uppercaseAlphabet:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
# This is the function that makes Caesar Cipher's magic!

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
# Reuses the encryption function, but inverts the "key" value to decrypt.

# Create the main function runCaesarCipherProgram
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Aphabet2: {myAlphabet2}')

    myMessage = getMessage()
    print(myMessage)

    myCipherKey = getCipherKey()
    print(myCipherKey)

    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')

    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')


# This function runs the entire Caesar Cipher program, calling all other functions in order.
# If you don’t do this… nothing happens!
runCaesarCipherProgram()