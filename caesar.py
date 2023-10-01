from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
print("----------------------------------------------------------")

def caesar(direction, plain_text, shift_amount):
    chipher_text = ""
    
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                if shift_amount <= 25:
                    new_position = position + shift_amount
                elif shift_amount >= 26:
                    new_position = position + (shift_amount % 26)    
            elif direction == "decode":
                if shift_amount <= 25:
                    new_position = position - shift_amount
                elif shift_amount >=26:
                    new_position = position - (shift_amount % 26)
            new_letter = alphabet[new_position]
            chipher_text += new_letter
        else:
            chipher_text += char

    if direction == "encode":  
        print(f"The encoded text is {chipher_text}")
    elif direction == "decode":
        print(f"The decoded text is {chipher_text}")

play_again = True
while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction=direction,plain_text=text, shift_amount=shift)
    
    question = input("Do you want to restart? Type 'yes' or 'no'.")
    if question == "no":
        play_again = False
        print("Goodbye")

