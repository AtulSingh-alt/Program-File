# Position Arguments
# def add(a,b):
#     c=a+b
#     print(f"Sum is {c}")
# add(5,6)
# add(4,3)



# Keyword Arguments
# def add(a,b):
#     c=a+b
#     print(f"Sum is {c}")
# add(a=5,b=4)
# add(8,b=7)

# Default Arguments
# def add(a,b,c=8):
#     d=a+b+c
#     print(f"Sum is {d}")
# add(5,4)
# add(8,7,6)

# Orbetory Arguments
# *args arguments

# def add(*number):
#     c=0
#     for i in number:
#         c+=i
#     print(f"Sum is {c}")
# add(5,4)
# add(8,7,6)
#

# **kwargs
# def info_person(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# info_person(name="Ram", age=30, dept="CSE")
# info_person(name="Shyam", dept="CSE")

#programs
# import math
# def paint_calculation(height,width,cover):
#     area = height*width
#     no_of_cans = math.ceil(area/cover)
#     print(f"You will need {no_of_cans} cans of paints.")
#
# h = int(input("Enter The height of wall in meters: \n"))
# w = int(input("Enter The width of wall in meters: \n"))
# coverage = 7
# paint_calculation(width=w, height=h, cover=coverage)

# 51) Caesar Cipher program

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