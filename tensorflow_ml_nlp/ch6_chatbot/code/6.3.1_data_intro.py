import pandas as pd

DATA_IN_PATH = 'C:/Users/kyucheol/Desktop/myfile/study/tensorflow_ml_nlp/6.CHATBOT/data_in/'
data = pd.read_csv(DATA_IN_PATH + './ChatBotData.csv', encoding = 'utf-8')

print(data.head())

sentences = list(data['Q']) + list(data['A'])

tokenized_sentences = [s.split() for s in sentences]
sent_len_by_token = [len(t) for t in tokenized_sentences]
sent_len_by_eumjeol = [len(s.replace(' ', '')) for s in sentences]

from konlpy.tag import Twitter
from konlpy.tag import Okt

okt = Okt()

morph_tokenized_sentences = [okt.morphs(s.replace(' ','')) for s in sentences]
sent_len_by_morph = [len(t) for t in morph_tokenized_sentences]

import matplotlib.pyplot as plt

plt.figure(figsize = (12, 5))
plt.hist(sent_len_by_token, bins = 50, range = [0,50], alpha = 0.5, color = 'r', label = 'eojeol')
plt.hist(sent_len_by_morph, bins = 50, range = [0,50], alpha = 0.5, color = 'g', label = 'morph')
plt.hist(sent_len_by_eumjeol, bins = 50, range = [0,50], alpha = 0.5, color = 'b', label = 'eumjeol')
plt.yscale('log')
plt.title('Sentene Length Histogram')
plt.xlabel('Sentence Length')
plt.ylabel('Number of Sentences')
plt.show()

import numpy as np

print('어절 최대 길이: {}'.format(np.max(sent_len_by_token)))
print('어절 최소 길이: {}'.format(np.min(sent_len_by_token)))
print('어절 평균 길이: {:.2f}'.format(np.mean(sent_len_by_token)))
print('어절 길이 표준편차: {:.2f}'.format(np.std(sent_len_by_token)))
print('어절 중간 길이: {}'.format(np.median(sent_len_by_token)))
print('제 1사분위 길이: {}'.format(np.percentile(sent_len_by_token,25)))
print('제 3사분위 길이: {}'.format(np.percentile(sent_len_by_token,75)))


plt.figure(figsize = (12,5))
plt.boxplot([sent_len_by_token, sent_len_by_morph, sent_len_by_eumjeol],
           labels = ['Eojeol', 'Morph', 'Eumjeol'],
           showmeans = True)
plt.show()

# 질문, 답변 각각에 대한 문장 길이 분포 분석

query_sentences = list(data['Q'])
answer_sentences = list(data['A'])

query_morph_tokenized_sentences = [okt.morphs(s.replace(' ','')) for s in query_sentences]
query_sent_len_by_morph = [len(t) for t in query_morph_tokenized_sentences]

answer_morph_tokenized_sentences = [okt.morphs(s.replace(' ','')) for s in answer_sentences]
answer_sent_len_by_morph = [len(t) for t in answer_morph_tokenized_sentences]

plt.figure(figsize=(12, 5))
plt.hist(query_sent_len_by_morph, bins = 50, range = [0,50], color = 'g', label = 'Query')
plt.hist(answer_sent_len_by_morph, bins = 50, range = [0,50], color = 'r', alpha = 0.5, label = 'Answer')
plt.legend()
plt.title('Query Length Histogram by Morph Token')
plt.xlabel('Query Length')
plt.ylabel('Num of Queries')
plt.show()

## 위의 그림을 보면 답변 데이터가 질문 데이터보다 좀 더 이상치 값이 많은 것을 확인할 수 있다. 


# 박스 플롯

plt.figure(figsize=(12, 5))
plt.boxplot([query_sent_len_by_morph, answer_sent_len_by_morph], labels = ['Query', 'Answer'])
plt.show()
#문장 최대길이를 정해야 하는데, 실제 통계를 반영한 길이를 그대로 넣었을 때 만족할 만한 성능을 얻기 힘듬, 디코더의 경우 문장 뒷부분이 일부 잘려서 생성하고자 하는 문장이 완전한 문장이 아닌 문제가 있을 수 있음. 경험적으로 25로 설정했을 때 괜찮~~.

okt.pos('오늘밤은 유난히 덥구나') # 품사를 구분함.

# 명사 형용사 동사만 쓸 것이기 때문에 그외의 단어는 제거하는 문자열을 만들자.

query_NVA_token_sentences = list()
answer_NVA_token_sentences = list()

for s in query_sentences:
    for token, tag in okt.pos(s.replace(' ','')):
        if tag == 'Noun' or tag == 'Verb' or tag =='Adjective':
            query_NVA_token_sentences.append(token)

for s in answer_sentences:
    temp_token_bucket = list()
    for token, tag in okt.pos(s.replace(' ','')):
        if tag == 'Noun' or tag == 'Verb' or tag =='Adjective':
            answer_NVA_token_sentences.append(token)

query_NVA_token_sentences = ' '.join(query_NVA_token_sentences)
answer_NVA_token_sentences = ' '.join(answer_NVA_token_sentences)

# 워드 클라우드

from wordcloud import WordCloud

query_wordcloud = WordCloud(font_path = DATA_IN_PATH + 'NanumGothic.ttf').generate(query_NVA_token_sentences)

plt.imshow(query_wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()

query_wordcloud = WordCloud(font_path = DATA_IN_PATH + 'NanumGothic.ttf').generate(answer_NVA_token_sentences)
plt.imshow(query_wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()
