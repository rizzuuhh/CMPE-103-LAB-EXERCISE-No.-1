import pyfiglet

# list all the characters
characters = "*&#+!"
key = "aeiou"
# ask the user's encrypted text
text = input("\033[34mEnter your encrypted text: \033[32m")

decrypt_text = ""
for letter in text:
    if letter.lower() in characters:
        decrypt_text += key[characters.find(letter.lower())]
    else:
        decrypt_text += letter
# print output
print(f"\033[91mDecrypted text: ")
print("*" * 70)
print(pyfiglet.figlet_format(decrypt_text))
print("*" * 70)



