alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Get the plaintext and keyword from the user
# Message: THISISTHELASTTASKHOORDAY
# Keyword: KNIGHTS
print("\033[92m:" * 40)
plain_text = input("Message: ")
key = input("Keyword: ")

# Repeat the keyword to match the length of the plaintext
repeated_keyword = key * (len(plain_text) // len(key) + 1)
keyword = repeated_keyword[:len(plain_text)]

ciphertext = ""
for i in range(len(plain_text)):
    plaintext_letter = plain_text[i]
    keyword_letter = keyword[i]
    plaintext_index = alphabet.index(plaintext_letter)
    keyword_index = alphabet.index(keyword_letter)
    ciphertext_index = (plaintext_index + keyword_index) % 26
    ciphertext_letter = alphabet[ciphertext_index]
    ciphertext += ciphertext_letter

# Print output
print("Ciphertext:", ciphertext)
print("\033[92m:" * 40)