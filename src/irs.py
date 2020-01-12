from preprocess import *
import os
from processor_pipeline import DocumentProcessor
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import math

docMetrics = {}


class DocId:
    ID = 0
    @staticmethod
    def assign():
        DocId.ID += 1
        return DocId.ID


docProcessor = DocumentProcessor()
# docProcessor.addProcessor(lambda word: SnowballStemmer('english').stem(word.token))
docProcessor.addProcessor(
    lambda word: WordNetLemmatizer().lemmatize(word.token, word.pos))


def extractDocMetrics(text, posting):
    metrics = {}
    freqDist = getFrequency(text)
    print(text)
    for key in freqDist:
        print(key)
        if key not in posting:
            pass
        # calculate the tf.idf coefficient per ratio
        wtf = 1 + math.log10(freqDist[key])
        widf = math.log10(DocId.ID/posting[key][1])
        metrics[key] = [wtf, widf, wtf*widf]
    return metrics


def batchExtractMetrics(corpus):
    termFreq = {}
    global docMetrics
    for text in corpus:
        txt = docProcessor.process(text)
        freqDist = getFrequency(txt)
        termFreq = mergeDict(termFreq, freqDist)
    docMetrics = termFreq
    return termFreq


def mergeDict(dict1, dict2):
    ''' Merge dictionaries and keep values of common keys in list'''
    # for key, value in dict2.items():
    #     dict2[key] = [value, 1]
    # dict3 = {**dict1, **dict2}

    # for key, value in dict3.items():
    #     if key in dict1 and key in dict2:
    #         # upadte term Frequencies
    #         dict3[key][0] = value[0] + dict2[key][0]
    #         dict3[key][1] = dict3[key][1] + 1
    id = DocId.assign()
    for key, value in dict2.items():
        if not key in dict1.keys():
            dict1[key] = [value, 1, (id, value)]
        else:
            dict1[key][0] += value
            dict1[key][1] += 1
            dict1[key].append((id, value))
    return dict1


def fetchAvailableDocuments():
    entries = os.listdir('./text/')
    return entries


def fetchDocuments(entries):
    corpus = []
    for entry in entries:
        with open('./text/' + entry, 'r')as f:
            corpus.append(f.read())
    return corpus


def calculateSimilarity(query, posting):
    # the result wrapper : a dictionary where the key is the docId and the value is the similarity to the query: key=>similarity
    total = {}
    # retrieve keys found in query from the posting and calculate the dot similarity
    for key in query:
        # weighted inverse document frequency (log10(N/DF))
        widf = query[key][1]
        # list of tuples containing (docId, tf)
        tagInfo = posting[key][2:]
        # calculate tf.idf(query) * tf.idf(document) for all document of that tag
        tagMetrics = [(x[0], query[key][2] * (x[1] * widf)) for x in tagInfo]
        # merge the result in total
        for x in tagMetrics:
            if x[0] in total.keys():
                total[x[0]] += x[1]
            else:
                total[x[0]] = x[1]
    print(total)
    return sorted(total, reverse=True)


def querySearch(query: str):
    global docMetrics
    processedQuery = docProcessor.process(query)
    queryMetrics = extractDocMetrics(processedQuery, docMetrics)

    docs = calculateSimilarity(queryMetrics, docMetrics)
    return docs


if __name__ == "__main__":
    entries = fetchAvailableDocuments()
    corpus = fetchDocuments(entries)
    # from nltk.book import text1
    # corpus = [' '.join(text1.tokens)]
    longText = "A good cook could cook as much cookies as a good cook who could cook cookies"
    text = "Best chocolate chip cookies recipe"

    corpus = [longText, text]
    freq = batchExtractMetrics(corpus)

    query = "chocolate cookies"
    processedQuery = docProcessor.process(query)
    queryMetrics = extractDocMetrics(processedQuery, freq)

    docs = calculateSimilarity(queryMetrics, freq)
    print(docs)
    # batchGetFrequencies()
