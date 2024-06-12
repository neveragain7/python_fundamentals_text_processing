text = input()

encrypted_text = ""

for letter in text:
    encrypted_letter = chr(ord(letter) + 3)
    encrypted_text += encrypted_letter

print(encrypted_text)
