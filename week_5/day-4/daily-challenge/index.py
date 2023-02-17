import string
import nltk
from nltk.corpus import stopwords

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        frequency = words.count(word)
        if frequency == 0:
            return None
        else:
            return f'The word "{word}" appears {frequency} times in the text.'

    def most_common_word(self):
        words = self.text.split()
        word_count = {}
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        most_common = max(word_count, key=word_count.get)
        return f'The most common word in the text is "{most_common}".'

    def unique_words(self):
        words = self.text.split()
        unique = list(set(words))
        return unique

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)

class TextModification(Text):
    def remove_punctuation(self):
        no_punc = self.text.translate(str.maketrans('', '', string.punctuation))
        return no_punc

    def remove_stopwords(self):
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))
        words = self.text.split()
        no_stopwords = [word for word in words if word.lower() not in stop_words]
        return ' '.join(no_stopwords)

    def remove_special_chars(self):
        no_special = ''.join(e for e in self.text if e.isalnum() or e.isspace())
        return no_special


text = Text("A good book would sometimes cost as much as a good house.")

print(text.word_frequency("good"))
print(text.most_common_word())
print(text.unique_words())

text = Text.from_file('the_stranger.txt')

modified_text = TextModification("This is some text with punctuation! And special characters #!$%^&*() and stopwords like a, an, the.")
print(modified_text.remove_punctuation())
print(modified_text.remove_stopwords())
print(modified_text.remove_special_chars())
