sequence = input()

result = ""

last_index = len(sequence) - 1

for index in range(0, len(sequence)):
    if index == last_index:
        result += sequence[index]
    elif sequence[index] == sequence[index + 1]:
        pass
    else:
        result += sequence[index]

print(result)
