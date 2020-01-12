import nltk
# nltk.download()
from nltk.tokenize import sent_tokenize
from nltk import FreqDist
from nltk import PorterStemmer
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english')) 


def getFrequency(text):
    return FreqDist(text)


def get_sents(text):
    return sent_tokenize(text)


def getLonguest(text):
    txtFreq = getFrequency(text)
    for word in txtFreq.keys():
        if len(word) > 5 and txtFreq[word] > 50:
            print(word)


def tokenize(text):
    return nltk.word_tokenize(text)


def text_toLower(text):
    return text.lower()


def pos_tag(tokens):
    # nltk.help.upenn_tagset()
    return nltk.pos_tag(tokens)


if __name__ == '__main__':
    # print(tokenize("Children shoudn't take sugary drinks before bed"))
    # print(get_sents("This is the first sentence. The cost of a bottle of milk in the U.S. is 2.99$. Is this the third sentence ? Yes, it is !"))

    longText = "marketing strategies carried out by U.S. companies for their agricultural chemicals, report Predictions for market share of such chemicals, or report market statistics for agrochemicals, PESTICIDE, herbicide, fungicide, insecticide, fertilizer, predicted sales, Market share, stimulate demand, PRICE cut, volume of sales"
    freq = getFrequency(tokenize(longText))
    # stemmer = PorterStemmer()
    # stem = stemmer.stem(lower_text(longText))

    # lemma = WordNetLemmatizer()
    # tokens = lemma.lemmatize(stem)
    # pos = pos_tag(tokens)
    # print(pos)
