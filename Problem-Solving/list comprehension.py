
word_list = ['cat', 'dog', 'rabbit']

letter_list = []

# for a_word in word_list:
#     for a_letter in a_word:
#         if a_letter not in letter_list:
#             letter_list.append(a_letter)

[[letter_list.append(i) for i in word if i not in letter_list] for word in word_list]
print(letter_list)
[print(i) for i in range(10)]