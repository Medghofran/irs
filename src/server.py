from app import app
from irs import batchExtractMetrics, docMetrics

def setup():
    longText = "A good cook could cook as much cookies as a good cook who could cook cookies"
    text = "Best chocolate chip cookies recipe"
    corpus = [longText, text]
    batchExtractMetrics(corpus)


app.before_first_request(setup)
