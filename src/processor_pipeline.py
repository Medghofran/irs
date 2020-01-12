from preprocess import *
from nltk.stem import SnowballStemmer


class Word:
    def __init__(self, token):
        self.token = token[0]
        if token[1].lower().startswith('v'):
            self.pos = 'v'
        elif token[1].lower().startswith('j'):
            self.pos = 'a'
        else:
            self.pos = 'n'
        pass

    def __str__(self):
        return self.token + ": " + self.pos


class DocumentProcessor:
    def __init__(self):
        self.__documentPipeline = []
        self.__tokenizer = tokenize
        self.__stopwords = stop_words
        self.__tokens = []

    def setTokenizer(self, tokenizer):
        self.__tokenizer = tokenizer

    def setStopWords(self, stopwords):
        self.__stopwords = stopwords

    def addProcessor(self, precessor):
        self.__documentPipeline.append(precessor)
        pass

    def getProcessInfo(self):
        for wordProcessor in self.__documentPipeline:
            print(wordProcessor)
            pass
        pass

    def __preprocessText(self, text):
        text = text_toLower(text)
        tokens = self.__tokenizer(text)
        pos = pos_tag(tokens)
        self.__tokens = [Word(w) for w in pos if not w[0] in self.__stopwords]

    def process(self, text: str):
        self.__preprocessText(text)
        result = self.__tokens
        for wordProcessor in self.__documentPipeline:
            step = []
            for word in result:
                word.token = wordProcessor(word)
                step.append(word)
            result = step
        return [w.token for w in result]


if __name__ == '__main__':

    longText = "marketing strategies carried out by U.S. companies for their agricultural chemicals, report Predictions for market share of such chemicals, or report market statistics for agrochemicals, PESTICIDE, herbicide, fungicide, insecticide, fertilizer, predicted sales, Market share, stimulate demand, PRICE cut, volume of sales"

    documentProcessor = DocumentProcessor()
    documentProcessor.addProcessor(
        lambda word: WordNetLemmatizer().lemmatize(word.token, word.pos))
    # documentProcessor.addProcessor(
    #     lambda word: SnowballStemmer('english').stem(word.token))
    processedText = documentProcessor.process(longText)
    print(processedText)
