import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

news = pd.read_csv("./data/abcnews-date-text.csv", error_bad_lines=False)
text = news[['headline_text']]

# 단어 토큰화
text['headline_text'] = text.apply(lambda row: word_tokenize(row['headline_text']), axis=1)

stop = stopwords.words('english')
# 불용어 제거
text['headline_text'] = text['headline_text'].apply(lambda x: [word for word in x if word not in (stop)])

# 표제어 추출
text['headline_text'] = text['headline_text'].apply(lambda x: [WordNetLemmatizer().lemmatize(word, pos='v') for word in x])

# 길이가 3 이하인 단어 제거
tokenized_doc = text['headline_text'].apply(lambda x: [word for word in x if len(word) > 3])
print(tokenized_doc[:5])

# 역토큰화 (토큰화 작업을 되돌림)
detokenized_doc = []
for i in range(len(text)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)

# 사이킷런의 TfidfVectorizer를 TF-IDF 행렬을 만들가
vectorizer = TfidfVectorizer(stop_words='english', max_features= 1000) # 상위 1,000개의 단어를 보존
X = vectorizer.fit_transform(text['headline_text'])

# 토픽 모델링
lda_model = LatentDirichletAllocation(n_components=10,learning_method='online',random_state=777,max_iter=1)
lda_top=lda_model.fit_transform(X)

terms = vectorizer.get_feature_names() # 단어 집합. 1,000개의 단어가 저장됨.

def get_topics(components, feature_names, n=5):
    for idx, topic in enumerate(components):
        print("Topic %d:" % (idx+1), [(feature_names[i], topic[i].round(2)) for i in topic.argsort()[:-n - 1:-1]])

get_topics(lda_model.components_,terms)

