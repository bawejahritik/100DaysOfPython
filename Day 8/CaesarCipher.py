logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    new_text = ""
    for i in text:
        idx = ord(i) - 97 + shift
        if(shift > 25):
            idx -= 26
        new_text += alphabet[idx]
    print(f"The encoded text is {new_text}")

def decrypt(text, shift):
    original_text = ""
    for i in text:
        idx = ord(i)-97-shift
        original_text += alphabet[idx]
    print(f"The decoded text is {original_text}")


user_choice = "yes"
print(logo)
while(user_choice == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction=="encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction=="decode":
        text = input("Type encoded message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    user_choice = input("Do you wish to continue? Yes or No?")