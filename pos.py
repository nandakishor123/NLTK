import nltk
from nltk.tokenize import PunktSentenceTokenizer #pre trained sentence tokenizer
from nltk.corpus import state_union

train_text = state_union.raw("2005-GWBush.txt") #training the PunctSentenceTokenizer
sample_text = state_union.raw("2006-GWBush.txt")

customm_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = customm_sent_tokenizer.tokenize(sample_text)
def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i) #tokenizing words
            tagged = nltk.pos_tag(words)  #tagging parts of speech
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()