letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)


# print(num_letters)
def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key
    for letter in text:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                # result+=letters[new_index]
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result


print()
print('*** CAESAR CIPHER PROGRAM *** ')
print('Do You Want To ENCRYPT OR DECRYPT? ')
user_input = input('e/d: ').lower()
print()
print()

try:
    if user_input == 'e':
        print('ENCRYPTION MODE SELECTED')
        key1 = int(input("enter key from 1 through 26: "))
        plaintext = input("enter text to encrypt: ")
        ciphertext = encrypt_decrypt(plaintext, user_input, key1)
        print('CIPHER TEXT: ', ciphertext)
    elif user_input == 'd':
        print('DECRYPTION MODE SELECTED ')
        key2 = int(input("enter key from 1 through 26: "))
        cipher_text = input("enter text to decrypt: ")
        plaintext = encrypt_decrypt(cipher_text, user_input, key2)
        print('CIPHER TEXT: ', plaintext)
    else:
        print('please enter either e or d')

except ValueError:
    print('please enter numeric value for the key')

        
