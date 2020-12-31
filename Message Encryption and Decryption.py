def get_input(n : int) -> int:
    """Returns the users input and checks if the input is a menu option

    >>> get_input(2)
    2
    >>> get_input(3) 
    3   
    """
    while True:
        #Checks if n is a menu option
        if n in [1, 2, 3]:
            return n
        else:
            #Asks for the input again if n is not a menu option
            print("\nInvalid choice. Try again.")
            n = (input("\n> "))
            if n == '1':
                return 1
            elif n == '2':
                return 2
            elif n == '3':
                return 3
            else:
                continue

def message_clean(msg : str) -> str:
    """Removes any non letters in the message and converts lowercase
    letters to uppercase
    
    >>> message_clean("Au75by")
    AUBY
    >>> message_clean("231><?>"<{98hi")
    HI
    """   
    counter = 0
    text_clean = ""

    for char in msg:

        #Checks if character is an uppercase letter
        if 65 <= ord(char) <= 90:
            text_clean += char
            counter += 1
            #Adds a space for every 5 letters
            if counter == 5:
                text_clean = text_clean + " "
                counter = 0
        #Converts lowercase letters to uppercase letter 
        elif 97 <= ord(char) <= 122:
            #Subtracts 32 from the characters ASCII value
            char = ord(char) - 32
            text_clean += chr(char)
            counter += 1
            if counter == 5:
                text_clean = text_clean + " "
                counter = 0
   
    return text_clean

def get_key(k : int) -> int:
    """Return key number after checking if the original input is valid

    >>>get_key(3)
    3
    >>>get_key(34)
    The key must be between 1 and 25(inclusive).
    Please enter a key number: 20
    """
    while True:
        #Checks if the key is valid
        if 1 <= k <= 25:
            return k
        else:
            print("The key must be between 1 and 25 (inclusive).")
                
            while True:
                try:
                    #Prompts user to enter a valid key value
                    k = int(input("Please enter a key: "))
                    break
                #Checks if the value entered is an integer
                except ValueError:
                    print("Not an integer. Try again.")
                    continue
            continue

def encrypt(text : str, shift : int) -> str:
    """Plaintext is encrypted due to each letters being shifted to the right
       based on the key number
       
    >>> encrypt(fardeen, 3)
    IDUGH HQ
    >>> encrypt(c0mput3r sc13nc3, 10)
    MWZED BCMXM
    """
    counter = 0
    e_text = ""
    p_text = message_clean(text)
    
    for char in p_text:

        #Checks if the character is uppercase 
        if 65 <= ord(char) <= 90:
            #Shifts value of plaintext to the right
            newc = chr(shift + ord(char))
            #Checks if character goes past "Z"
            if ord(newc) > 90:
                #Starts shifting again from "A"
                newc = chr(64 + ord(newc) - 90)
                e_text += newc
                counter += 1
                if counter == 5:
                    e_text += " "
                    counter = 0
            else:
                e_text += newc
                counter += 1
                if counter == 5:
                    e_text += " "
                    counter = 0
                
    return e_text

def decrypt(text: str, shift: int) -> str:
    """Ciphertext is decrypted due to each letters being shifted to the left
    based on the key number
    >>> decrypt("ifmmp", 1)
    HELLO
    >>> decrypt("mubtasim", 2)
    KSZRY QGK
    """
    counter = 0
    d_text = ""
    cipher_text = message_clean(text)
    
    for char in cipher_text:
        
        #Checks if the character is uppercase
        if 65 <= ord(char) <= 90:
            #Checks if character goes past "A"
            c = chr(ord(char) - shift)
            if ord(c) < 65:
                #Starts shifting again from "Z"
                c = chr(91 - (65 - ord(c)))
                d_text += c
                counter += 1
                if counter == 5:
                    d_text += " "
                    counter = 0
            else:
                d_text += c
                counter += 1
                if counter == 5:
                    d_text += " "
                    counter = 0

    return d_text

def main():
    """The main function that contains the user interface"""
    while True:
        print("""\n----------------------------------
EasyCrypt Text Encryptor/Decryptor
----------------------------------

Please choose from one of the following menu options:
1. Encrypt plaintext.
2. Decrypt ciphertext.
3. Exit.""")

        #Checks if the input is an integer
        while True:
            try:
                choice = int(input("\n> "))
                break
            except ValueError:
                print("\nInvalid choice. Try again.")
                continue
            
        x = get_input(choice)

        if x == 1:
            msg = input("\nPlease enter text to encrypt: ")
            print("This is the plaintext: {}".format(message_clean(msg)))
            text = message_clean(msg)

            print("\nAn encryption key is an integer between 1 and 25")
            while True:
                try:
                    shift = int(input("Please enter a key: "))
                    break
                except ValueError:
                    print("Not an integer. Try again.")
                    continue

            key = get_key(shift)
            
            print("\nYour message has been encrypted: {}".format(encrypt(text, key)))
            continue

        elif x == 2:
            msg = input("\nPlease enter text to decrypt: ")
            print("This is the ciphertext: {}".format(message_clean(msg)))
            text = message_clean(msg)

            print("\nAn decryption key is an integer between 1 and 25")
            while True:
                try:
                    shift = int(input("Please enter a key: "))
                    break
                except ValueError:
                    print("Not an integer. Try again.")
                    continue
                
            key = get_key(shift)
            
            print("\nYour message has been decrypted: {}".format(decrypt(text, key)))
            continue
            
        else:
            break

main()



        
