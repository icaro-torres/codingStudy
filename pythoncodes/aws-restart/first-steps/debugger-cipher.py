# this is a test Caesar Cipher program to run with debugging in mind

# funccion to get a double alphabet
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# funccion to get a message from the user
def getMessage():
    stringToEncrypt = input("Please, enter a message to encrypt: ")
    return stringToEncrypt

# funccion to get a cipher key from the user
def getCipherKey():
    shiftAmount = input("Please, enter a cipher key (number of 1 to 25): ")
    return shiftAmount

# funccion to ENCRYPT a message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper() # convert the message to uppercase
    for currentCharacter in uppercaseMessage: # for each character in the message
        position = alphabet.find(currentCharacter) # find the position of the character in the alphabet
        # this is the line with the defect 1: it should be int(cipherKey) but it is not
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition] # take a new character from the alphabet
        else:
            encryptedMessage = encryptedMessage + currentCharacter # keep the character as is if not in alphabet
    # if the new position is out of bounds, wrap around
    return encryptedMessage

# function to DECRYPT a message
def decryptMessage(message, cipherKey, alphabet):
    # to decrypt, we need to reverse the cipher key
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet) # reuse the encrypt function with a negative key

# the main function to run the caesar cipher program
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alfabeto: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alfabeto Duplicado: {myAlphabet2}')

    myMessage = getMessage()
    print(f'Mensagem original: {myMessage}')

    myCipherKey = getCipherKey()
    print(f'Chave informada: {myCipherKey}')

    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Mensagem Criptografada: {myEncryptedMessage}')

    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Mensagem Descriptografada: {myDecryptedMessage}')

# here is where the real program starts
runCaesarCipherProgram()