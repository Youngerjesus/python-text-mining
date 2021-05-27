import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Mecab
from sklearn.decomposition._nmf import NMF

def tokenizer(text):
    nouns = mecab.nouns(text)
    return [noun for noun in nouns if len(noun) > 1]


mecab = Mecab()

topNews = pd.read_csv("data/8월 1면 뉴스.csv")
print(topNews['media'].unique())

tfIdVectorizer = TfidfVectorizer(tokenizer=tokenizer,
                                 max_df=0.90,
                                 min_df=2,
                                 max_features=5000)
print(topNews['text'])
tfidf = tfIdVectorizer.fit_transform(topNews['text'])

nmf = NMF(n_components=8, random_state=3)
H = nmf.fit_transform(tfidf)
W = nmf.components_

def printTopics(W,H,words,titles,nTopTitles=5,nTopWords=10):
    for topicIndex, (docVec, wordVec) in enumerate(zip(H,W)):
        message = "\nTopic %d" % topicIndex
        message += " #" + " #".join([words[i] for i in wordVec.argsort()[:-nTopWords - 1: -1]])

        message += "\n\n"
        message += "    \n".join([titles[i] for i in docVec.argsort()[:-nTopTitles - 1 : -1]])
        print(message)

printTopics(W,H,tfIdVectorizer.get_feature_names(), topNews['title'])
