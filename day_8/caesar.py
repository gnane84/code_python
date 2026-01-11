import art



alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]


# Individual function for each encode and decode

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for char in original_text:
#         shifted_position = alphabet.index(char) + shift_amount
#         cipher_text += alphabet[shifted_position % 26]
#     print(f" Here is the encoded test: {cipher_text}")
#
# encrypt(original_text=text, shift_amount=shift)
#
# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for char in original_text:
#         shifted_position = alphabet.index(char) - shift_amount
#         output_text += alphabet[shifted_position % 26]
#     print(f" Here is the encoded test: {output_text}")
#
# decrypt(original_text=text, shift_amount=shift)
#

# combined function for both encode and decode

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for char in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        shifted_position = alphabet.index(char) + shift_amount
        output_text += alphabet[shifted_position % len(alphabet)]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

continue_cipher = True

while continue_cipher:

    direction = input(f"Type 'encode' to encrypt or 'decode' to decrypt:\n ").lower()

    if direction not in ["encode", "decode"]:
        print("Please type 'encode' or 'decode'.")
        continue

    text = input(f"Type your message:\n ").lower()
    shift = int(input(f"Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input(f"Type 'yes' if you want to continue again. Otherwise, type no.:\n ").lower()
    if restart == "no":
        continue_cipher = False
        print(f"Goodbye")
