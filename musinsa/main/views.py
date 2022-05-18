from django.shortcuts import render
from django.http import HttpResponse
import pickle
# 상위 폴더에서 가져오기

# top10_lst = mus.top10
# top10 = {}
# for i in top10_lst:
#     top10[i[0]] = i[1]

# Create your views here.

with open("/Users/cmblir/Python/Musinsa-Analysis/musinsa/main/pickles/top10_words.pickle", 'rb') as f:
    top10 = pickle.load(f)

def index(request):
    return render(request, 'index.html', {'top10' : top10})