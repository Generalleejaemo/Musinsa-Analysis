from django.shortcuts import render
from django.http import HttpResponse
import os, sys
import pickle
import re
import Tokenizer

tokenizer = Tokenizer(vocab_size) 
# 상위 폴더에서 가져오기

# top10_lst = mus.top10
# top10 = {}
# for i in top10_lst:
#     top10[i[0]] = i[1]
def sentiment_predict(new_sentence):
  new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
  new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
  new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
  encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
  pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
  score = float(loaded_model.predict(pad_new)) # 예측
  if(score > 0.5):
    print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
  else:
    print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))
# Create your views here.

with open("main/top10_words.pickle", 'rb') as f: # 상위 언급 10개 단어
    top10 = pickle.load(f)
with open("main/bad_top10_words.pickle", 'rb') as f: # 낮은 평점기반 상위 언급 10개 단어
    bad_top10 = pickle.load(f)
with open("main/good_top10_words.pickle", 'rb') as f: # 높은 평점기반 상위 언급 10개 단어
    good_top10 = pickle.load(f)
with open("main/model.pickle", "rb") as f: # 사용할 모델
    model = pickle.load(f)

def index(request):
    return render(request, 'index.html')
# {'top10' : top10, 'bad_top10' : bad_top10, 'good_top10' : good_top10})

def top10_html(request):
    return render(request, 'top10.html', {'top10' : top10})

def bad_top10_html(request):
    return render(request, 'bad10.html', {'top10' : bad_top10})

def good_top10_html(request):
    return render(request, 'good10.html', {'top10' : good_top10})

def reviews_html(request):
    return render(request, 'review.html', {'model' : model})