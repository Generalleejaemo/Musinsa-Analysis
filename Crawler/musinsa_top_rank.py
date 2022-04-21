# 상위 랭킹 브랜드 크롤링
from selenium import webdriver
import chromedriver_autoinstaller
import time
import csv

with open('top_brands.csv', 'w') as file: # csv파일 만들기
    file.write("Brand_name" + '\n')

'''
무신사 상위랭크 카테고리별 코드
데님팬츠 : 003002
코튼팬츠 : 003007

'''
with open('')

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

try: # 크롬 드라이버
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver')   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver')

driver.implicitly_wait(10) # 10초정도 멈추기

def top_brands(): # 브랜드 정보 불러오기
    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver')
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver')
    for i in range(1, 101): # 1페이지부터 100페이지까지
        driver.get(f'https://www.musinsa.com/ranking/best?period=now&age=ALL&mainCategory=&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page={i}&viewType=small&priceMin=&priceMax=')
        time.sleep(0.1)
        for i in range(1, 91): # 각 페이지별 90등까지
            brand_name = driver.find_element_by_css_selector(f'#goodsRankList > li:nth-child({i}) > div.li_inner > div.article_info > p.item_title > a')
            with open('musinsa_top_brands.csv', 'a') as file:
                file.write(brand_name.text + '\n')
    driver.quit()

# top_brands() 상위 9000등까지 랭크한 아이템 브랜드
