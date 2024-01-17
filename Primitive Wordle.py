secret_word = "secret"  # Replace with your own word
guess = "easycr"
hint = ""
for i, letter in enumerate(guess):
    if letter == secret_word[i]:
        hint += letter.upper()
    elif letter in secret_word:
        hint += letter.lower()
    else:
        hint += "_"
print(hint)
