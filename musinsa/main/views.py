import datetime

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import os
import sys
import pickle
import re
import tensorflow as tf
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer

class check_review():
    tokenizer = Tokenizer()
    okt = Okt()
    total_cnt = len(tokenizer.word_index)  # 단어의 수
    rare_cnt = 0  # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
    vocab_size = total_cnt - rare_cnt + 1
    max_len = 30
    loaded_model = load_model('main/best_model.h5')
    stopwords = ['좋아요', '옷', '좀', '것', '바지', '구매', '같아요', '생각', '터', '구매', '아우', '평점', "좋고", "입니다", "더", "좋습니다", "거", "떄", "좋은", "맘", "입", "비", "길이", "조금", "진짜", "마음", "수", "제", "아주", "살짝", "자주", "감", "정말", "안", "같습니다", "드", "정도", "그냥", "코드", "티", "약간", "어", "하나", "얇아서", "라피", "저", "낫", "지금", "요즘", "처음", "이",
                 "있어서", "디스", "완전", "버댓", "부분", "다른", "용", "역시", "굿", "키", "고민", "있는", "사진", "크게", "있어요", "듭니다", "어깨", "에스", '높은', '남성', '하의', '상의', '여성', '스탠다드', '이뻐요', '때', '예뻐요', '버핏', '이쁘고', '스토어', '좋네요', '편하게',
                '무난', '편하고', '만족합니다', '예일', '소재', '날씨', '제품', '예쁘고', '이쁩니다', '듭니', '이쁘네요', '색도', '통', '최고', '듯',
                '토피', '만족', '와릿이즌', '그레이', '리', '같네요', '같은', '오버', '적당히', '적당하고', '적당한', '이뻐서', '요', '가을', '나인', '별로', '아디다스', '팔', '셔츠', '예쁩니다', '편이', '엘무드',
                '엄브로', '트', '분', '스튜디오', '폴로', '후드', '품', '커서', '피오', '블랙', '도', '가디건', '또', '원하던', '얇고', '편해요', '예뻐서', '스컬', '프터', '상품', '걱정', '의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']
    def sentiment_predict(new_sentence):
        new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', new_sentence)
        new_sentence = check_review.okt.morphs(new_sentence, stem=True)  # 토큰화
        new_sentence = [
            word for word in new_sentence if not word in check_review.stopwords]  # 불용어 제거
        encoded = check_review.tokenizer.texts_to_sequences([new_sentence])  # 정수 인코딩
        pad_new = pad_sequences(encoded, maxlen=check_review.max_len)  # 패딩
        score = float(check_review.loaded_model.predict(pad_new))  # 예측
        if(score > 0.5):
            print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
        else:
            print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))
# 상위 폴더에서 가져오기

# top10_lst = mus.top10
# top10 = {}
# for i in top10_lst:
#     top10[i[0]] = i[1]


# Create your views here.


with open("main/top10_words.pickle", 'rb') as f:  # 상위 언급 10개 단어
    top10 = pickle.load(f)
with open("main/bad_top10_words.pickle", 'rb') as f:  # 낮은 평점기반 상위 언급 10개 단어
    bad_top10 = pickle.load(f)
with open("main/good_top10_words.pickle", 'rb') as f:  # 높은 평점기반 상위 언급 10개 단어
    good_top10 = pickle.load(f)
with open("main/model.pickle", "rb") as f:  # 사용할 모델
    model = pickle.load(f)


def index(request):
    return render(request, 'index.html')
# {'top10' : top10, 'bad_top10' : bad_top10, 'good_top10' : good_top10})


def top10_html(request):
    return render(request, 'top10.html', {'top10': top10})


def bad_top10_html(request):
    return render(request, 'bad10.html', {'top10': bad_top10})


def good_top10_html(request):
    return render(request, 'good10.html', {'top10': good_top10})

def predict(request):
    return render(request, 'predict.html')

def reviews_html(request):
    data = request.form['a']
    check = check_review()
    pred = check.sentiment_predict(data)
    return render(request, 'review.html', {'model': model}, pred=pred)
