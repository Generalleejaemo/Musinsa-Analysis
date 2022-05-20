import os
import sys
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from konlpy.tag import Twitter
from collections import Counter
from konlpy.tag import Okt
import pickle


def get_font_family():
    '''
    시스템 환경에 따른 기본 폰트명을 반환하는 함수
    '''
    import platform
    system_name = platform.system()

    if system_name == 'Darwin' :
        font_family = 'AppleGothic'
    elif system_name == 'Windows':
        font_family = 'Malgun Gothic'
    else:
        # Linux(colab)
        # !apt-get install fonts-nanum -qq > /dev/null
        # !fc-cache -fv

        import matplotlib as mpl
        mpl.font_manager._rebuild()
        findfont = mpl.font_manager.fontManager.findfont
        mpl.font_manager.findfont = findfont
        mpl.backends.backend_agg.findfont = findfont

        font_family = 'NanumBarunGothic'

    return font_family

def show_plt():
    # style 설정은 꼭 폰트설정 위에서 한다. 
    # style에 폰트 설정이 들어있으면 한글폰트가 초기화 되어 깨진다.
    plt.style.use('seaborn')

    #폰트설정
    plt.rc('font', family=get_font_family())

    #마이너스폰트 설정
    plt.rc('axes', unicode_minus=False)

    # 그래프에 retina display 적용
    # 그래프 해상도 
    from IPython.display import set_matplotlib_formats
    set_matplotlib_formats('retina')

# 추후 실시간 크롤링 후 데이터 워딩할 때 사용할 함수 정의
def word_analysis():

    Okt = Okt()
    text = open('Musinsa-Analysis/Analysis/reviews.txt').read()
    bad_reviews = open('Musinsa-Analysis/Analysis/bad_reviews.txt').read()
    good_reviews = open('Musinsa-Analysis/Analysis/good_reviews.txt').read()
    sentences_tag = []
    sentences_tag = Okt.pos(text)
    bad_sentences_tag = Okt.pos(bad_reviews)
    good_sentences_tag = Okt.pos(good_reviews)

    noun_adj_list = []

    for word, tag in sentences_tag:
        if tag in ['Noun' , 'Adjective']: 
            noun_adj_list.append(word)

    good_noun_adj_list = []

    for word, tag in good_sentences_tag:
        if tag in ['Noun' , 'Adjective']: 
            good_noun_adj_list.append(word)

    bad_noun_adj_list = []

    for word, tag in bad_sentences_tag:
        if tag in ['Noun' , 'Adjective']: 
            bad_noun_adj_list.append(word)

    counts = Counter(noun_adj_list)
    tags = counts.most_common(40) 

    top10 = [i for i in tags[:10]]

with open('/Users/cmblir/Python/Musinsa-Analysis/Analysis/top10_words.pickle', 'rb') as f:
    top10 = pickle.load(f)