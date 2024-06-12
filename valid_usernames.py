usernames = input().split(", ")
letters_are_ok = True

for word in usernames:
    if 3 <= len(word) <= 16:
        for letter in word:
            if not letter.isalpha() and not letter.isdigit() and not letter == "-" and not letter == "_":
                letters_are_ok = False
                break
        if letters_are_ok:
            print(word)
        letters_are_ok = True
