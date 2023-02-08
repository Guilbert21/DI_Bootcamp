word = input("Enter a word: ")

char_index = {}

for index, letter in enumerate(word):
    if letter in char_index:
        char_index[letter].append(index)
    else:
        char_index[letter] = [index]

print(char_index)




