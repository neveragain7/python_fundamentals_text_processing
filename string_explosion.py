text = input()

result = ""
strength = 0

for index in range(0, len(text)):
    if text[index].isdigit() and text[index - 1] == ">":
        strength += int(text[index])
        strength -= 1
        continue

    if strength > 0 and not text[index] == ">":
        strength -= 1
    else:
        result += text[index]

print(result)
