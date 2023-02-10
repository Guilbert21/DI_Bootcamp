def sort_words(words):
    words_list = words.split(',')
    sorted_words = [word for word in sorted(words_list)]
    return ','.join(sorted_words)

words = input("Enter a comma-separated sequence of words: ")
print(sort_words(words))

