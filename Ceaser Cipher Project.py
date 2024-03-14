#List representin the alphabet, includin a repetion for easy shifting
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x,' 'y', 'z']

#Prompting user for the direction of encryption/decryption, the text, and the shift amount
direction = input("Type 'encode' to encrypt, type 'decode' to decyrpt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Function to perform the Caesar cipher
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
#Shifting text based on the direction (encoding or decoding)
    if cipher_direction == "decode":
        shift_amount = -1
#Loop through each character in the text
    for char in start_text:
#Check if the character is in the alphabet
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
#If the character is not in the alphabet (e.g., space or symbol), keep it unchanged
            end_text =+ char
#Printing the result
    print(f"The {cipher_direction}d text is {end_text}")

#Loop to continue the cipher program if the user wants to
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to dcrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    
#Ensuring the shift is within the range of the alphabet.
    shift = shift % 26

#Calling the caeser function with user inputs
    ceaser(start_text=text, shift_amount=shift, cipher_direction=direction) 

#Asking the user if they want to continue
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")
    

  
    
