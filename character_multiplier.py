words = input().split()

total_sum = 0
lengths_are_equal = False
first_word = words[0]
second_word = words[1]

shortest_length = min(len(first_word), len(second_word))

for index in range(0, shortest_length):
    result = ord(first_word[index]) * ord(second_word[index])
    total_sum += result

if len(first_word) > shortest_length:
    longest_word = first_word
elif len(second_word) > shortest_length:
    longest_word = second_word
else:
    lengths_are_equal = True
    longest_word = first_word

if not lengths_are_equal:
    for index in range(shortest_length, len(longest_word)):
        total_sum += ord(longest_word[index])

print(total_sum)
