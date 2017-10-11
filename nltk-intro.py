from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello, there! How are you ? I hope you are fine :)"

print(sent_tokenize(example_text)) #tokenize the string sentence wise
print(word_tokenize(example_text)) #tokeize the string word wise.
for i in word_tokenize(example_text):
   print(i)