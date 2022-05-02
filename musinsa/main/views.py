from django.shortcuts import render
from django.http import HttpResponse

# import import_ipynb # ipynb를 py 형태로 변환해서 가져오기
import sys
sys.path.append(r'/Users/cmblir/Python/Musinsa-Analysis') # sys로 최상위 폴더 추가
from Analysis import musinsa_py as mus# 상위 폴더에서 가져오기

# top10_lst = mus.top10
# top10 = {}
# for i in top10_lst:
#     top10[i[0]] = i[1]

# Create your views here.
def index(request):
    top10_lst = mus.top10
    top10 = {}
    for i in top10_lst:
        top10[i[0]] = i[1]
    return render(request, 'index.html', {'top10' : top10})