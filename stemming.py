#Stemming reffers to the act of breaking down the word to its root from. For eg: the word ridden, riding can be brought down to rid.

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

#example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

 
example_string = "All pythoners have pythoned the pythoning poorly!"

words = word_tokenize(example_string)

for w in words:
    print(ps.stem(w))
