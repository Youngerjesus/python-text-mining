import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag import Mecab

mecab = Mecab()

def tokenizer(text):
    nouns = mecab.nouns(text)
    return [noun for noun in nouns if len(noun) > 1]

countVectorizer = CountVectorizer(tokenizer=tokenizer)

news = pd.read_csv("./data/전처리_샘플뉴스.csv")
countVectorizer.fit(news['text'])
print(countVectorizer.get_feature_names()[:20])
print(countVectorizer.fit_transform(news['text']).toarray())
print(countVectorizer.get_feature_names())
print(countVectorizer.vocabulary_)