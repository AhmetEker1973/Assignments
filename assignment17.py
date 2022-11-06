from itertools import count

sentence = input("Please enter a sentence: ").lower()

letter_count_map = {}

for i in sentence :
    letter_count_map[i] = sentence.count(i)

print(letter_count_map)

Please enter a sentence: hippo runs to us!
{'h': 1, 'i': 1, 'p': 2, 'o': 2, ' ': 3, 'r': 1, 'u': 2, 'n': 1, 's': 2, 't': 1, '!': 1}
Please enter a sentence: Today's assignment is adding letters into a map!!!
{'t': 5, 'o': 2, 'd': 3, 'a': 5, 'y': 1, "'": 1, 's': 5, ' ': 7, 'i': 4, 'g': 2, 'n': 4, 'm': 2, 'e': 3, 'l': 1, 'r': 1, 'p': 1, '!': 3}
