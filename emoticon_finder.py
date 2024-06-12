text = input()

emoticon = ""

for index in range(0, len(text)):
    if text[index] == ":":
        emoticon += text[index] + text[index+1]
        print(emoticon)
        emoticon = ""