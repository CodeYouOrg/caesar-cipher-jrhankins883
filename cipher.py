text = 'programming'
shift = 5
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text:
    index = alphabet.find(char)
    new_index = (index + shift) % 26
    encrypted_text += alphabet[new_index]
print(encrypted_text)