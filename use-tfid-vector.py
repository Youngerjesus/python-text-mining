import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Mecab
from wordcloud import WordCloud

def tokenizer(text):
    nouns = mecab.nouns(text)
    return [noun for noun in nouns if len(noun) > 1]

mecab = Mecab()
wordcloud = WordCloud(
    width=300,
    height=300,
    max_words=50,
    background_color="white"
)
tfIdVectorizer = TfidfVectorizer(tokenizer=tokenizer)

news = pd.read_csv("./data/전처리_샘플뉴스.csv")
tfIdMatrix = tfIdVectorizer.fit_transform(news['text'])

plt.figure(figsize=(30,5))
for i,index in enumerate([0,1,2,3,4]):
    value = tfIdMatrix[index].toarray().squeeze()
    key = tfIdVectorizer.get_feature_names()
    score = dict(zip(key,value))
    wordcloud.generate_from_frequencies(score)
    arr = wordcloud.to_array()
    plt.subplot(1,5,i+1)
    plt.imshow(arr)
    plt.axis("off")