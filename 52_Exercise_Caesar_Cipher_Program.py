# # 51) Caesar Cipher program

import string

alp = string.ascii_letters
def encryption(plain_text, shift_key):
    cipher_text =""
    for char in plain_text:
        if char in alp:
            position = alp.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alp[new_position]
        else:
            cipher_text+= char
    print(f"Here is the text after encryption: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text =""
    for char in cipher_text:
        if char in alp:
            position = alp.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alp[new_position]
        else:
            plain_text += char
    print(f"Here is the text after decryption: {plain_text}")

wanna_end = False
while not wanna_end:
    what_to_do = input("type 'encrypt' for encryption, type 'decrypt' for decryption: \n")
    text = input("Type you message: \n")
    shift = int(input("Enter the shift key: \n"))
    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(text, shift)
    play_again = input("Type 'yes' to continue, type 'no' to exit")
    if play_again == 'no':
        wanna_end=True
        print("have a nice day! Bye...")