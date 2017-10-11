from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example to show off stop word filteration."

stop_words = set(stopwords.words("english")) #make a set of all the stop words

words = word_tokenize(example_sentence)
filtered_sentence = [] #declaring empty array for filtered sentences

for w in words: # creates a set of filtered words. ie word in the sammple sentence which are not stop words.
    if w not in stop_words:
        filtered_sentence.append(w)

print filtered_sentence