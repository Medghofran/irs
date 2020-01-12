from bs4 import BeautifulSoup
import requests
import urllib.request
import time
# utility for reading pdf files as text
import textract

BASE_URL = "https://arxiv.org/"
# different research paper categories that would be downloaded.
CATEGORIES = {
    "Astrophysics": "list/astro-ph/recent",
    "Condensed Matter": "list/cond-mat/recent",
    "General Relativity and Quantum Cosmology": "list/gr-qc/recent",
    "High Energy Physics - Phenomenology": "list/hep-ph/recent",
    "Nuclear Theory": "list/nucl-th/recent",
    "Mathematics": "list/math/recent",
    "Computing Research Repository": "list/corr/recent",
}


def hasTag(tag):
    return tag.name == 'a' and tag.get_text() == 'pdf'


def download(fileUrl):
    fileName = fileUrl.split('/')[2]
    filePath = "./library/" + fileName + ".pdf"
    urllib.request.urlretrieve(
        BASE_URL + fileUrl, filePath)
    return filePath, fileName


def extractText(filePath, fileName):
    # creating an object
    text = textract.process(
        filePath, method='pdfminer').decode().replace('\n', ' ')
    with open("./text/" + fileName + ".txt", "w+") as f:
        f.write(text)


def buildDataset():
    for category in CATEGORIES:
        print("###", category, "###")
        catUrl = CATEGORIES[category]
        # get raw html data
        response = requests.get(BASE_URL + catUrl)
        # create parsed html dictionnary
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.findAll(hasTag)
        try:
            for link in links:
                filePath, fileName = download(link.get('href'))
                print(fileName)
                extractText(filePath, fileName)
        except:
            pass


if __name__ == '__main__':
    buildDataset()
