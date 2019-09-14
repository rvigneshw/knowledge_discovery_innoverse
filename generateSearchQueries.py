import spacy
import os
import fetchFromWeb
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
OUTPUT_DIR="CollectedData"

nlp=spacy.load('en_core_web_sm')
# doctext=open('extractedText.txt','rb')
exceptionList=["CARDINAL","PERCENT"]
with open('extractedText.txt', 'r') as file:
        data = file.read().replace('\n', '')
doc=nlp(data)

def generateTheKeywords():
    # with open('extractedText.txt', 'r') as extractedTextFile:
    #     data = extractedTextFile.read().replace('\n', '')
    doc=nlp(data)
    ent_rel=[]
    ent_rel=[(ent.label_,ent.text) for ent in doc.ents]
    # for ent in ent_rel:
    #     print("{}-{}".format(ent[0],ent[1]))
    with open('searchQueries.txt', 'w') as searchQueryFile:
        text=''
        for ent in ent_rel:
            if ent[0] not in exceptionList:
                text=text+"{}+{}\n".format(ent[0],ent[1])
        searchQueryFile.write(text)

def generateSummary():    
    summary=''
    mytokens = [token.text for token in doc]
    stopwords = list(STOP_WORDS)
    word_frequencies = {}
    for word in doc:
        if word.text not in stopwords:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
    sentence_list = [ sentence for sentence in doc.sents ]
    sentence_scores = {}  
    for sent in sentence_list:  
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if len(sent.text.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word.text.lower()]
                        else:
                            sentence_scores[sent] += word_frequencies[word.text.lower()]
    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    for w in summarized_sentences:
        summary=summary+str(w.text)
    with open(os.path.join(OUTPUT_DIR, 'summary.html'), 'w+') as summaryfile:
        summaryfile.write(summary)
    # return summary



if __name__ == "__main__":
    generateSummary()
    generateTheKeywords()
    # fileAndData()
