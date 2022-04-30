# 상위 랭킹 브랜드 크롤링
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller
import time
import csv
"""
click()이 안될시 사용
from selenium.webdriver.common.keys import Keys
send_keys(Keys.ENTER)
"""


# 크롬 버젼 확인 후 새로운 드라이버 설치해서 실행
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito") # 시크릿 모드
chrome_options.add_argument("--headless") # 리눅스 GUI 없는 디스플레이 모드
chrome_options.add_argument("--no-sandbox") # 리소스에 대한 엑서스 방지
chrome_options.add_argument("--disable-setuid-sandbox") # 크롬 충돌 방지
chrome_options.add_argument("--disable-dev-shm-usage") # 메모리 부족 에러 방지
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

try: # 크롬 드라이버
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', chrome_options=chrome_options)   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', chrome_options=chrome_options)

# WebDruverException Error 방지 기존의 드라이버 버젼으로 지정
# driver = webdriver.Chrome(executable_path='/Users/cmblir/Python/Musinsa-Analysis/100/chromedriver')
driver.implicitly_wait(10) # 10초정도 멈추기

def popular_items(): # 인기있는 카테고리의 무신사가 추천해주는 브랜드 리스트 뽑기
    # 각 카테고리별 상위 브랜드 분석
    popular_dict = {"데님팬츠": "003002",
                "코튼팬츠": "003007",
                "긴팔 티셔츠": "001010",
                "컨버스/단화": "018002",
                "로퍼": "005015",
                "선글라스": "009001",
                "러닝화/피트니스화": "018003",
                "민소매 티셔츠": "001011",
                "슈트 팬츠/슬랙스": "003008",
                "트레이닝/조거 팬츠": "003004",
                "향수/탈취": "015007",
                "캠핑용품": "017028"
                }
    # want = f"{input('원하시는 상품을 입력해주세요 : ')}"
    time.sleep(0.1)
    f = open("popular_items.csv", 'w')
    csv_popular_items = csv.writer(f)
    csv_popular_items.writerow(["category", "popular_items_brand_name"])
    for want in popular_dict.keys():
        # with open('popular_items.csv', 'w') as file:
        #     file.write(f"Category, Brand_name")
        driver.get(f'https://www.musinsa.com/category/{popular_dict[want]}')
        for i in range(2, 11): # 각각 무신사가 추천한 1000개의 데이터만
            driver.get(f'https://www.musinsa.com/category/018002?d_cat_cd=018002&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page={i}&display_cnt=90&sale_goods=&group_sale=&kids=N&ex_soldout=&color=&price1=&price2=&exclusive_yn=&shoeSizeOption=&tags=&campaign_id=&timesale_yn=&q=&includeKeywords=&measure=')
            time.sleep(0.1)
            for i in range(1, 91):
                brand_name = driver.find_element_by_css_selector(f'#searchList > li:nth-child({i}) > div.li_inner > div.article_info > p.item_title > a')
                csv_popular_items.writerow([want, brand_name.text])
    driver.quit()


def top_brands(): # 상위 브랜드 분석
    # with open('top_brands.csv', 'w') as file: # csv파일 만들기
    #     file.write("Brand_name")
    f = open('top_brands.csv', 'w')
    csv_top_brands = csv.writer(f)
    csv_top_brands.writerow(["top_brands_brand_name"])
    for i in range(1, 101): # 1페이지부터 100페이지까지
        driver.get(f'https://www.musinsa.com/ranking/best?period=now&age=ALL&mainCategory=&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page={i}&viewType=small&priceMin=&priceMax=')
        time.sleep(0.1)
        for i in range(1, 91): # 각 페이지별 90등까지
            brand_name = driver.find_element_by_css_selector(f'#goodsRankList > li:nth-child({i}) > div.li_inner > div.article_info > p.item_title > a')
            # with open('musinsa_top_brands.csv', 'a', newline = '') as file:
            #     file.write(brand_name.text + "\n")
            csv_top_brands.writerow([brand_name.text])
    driver.quit()

def rank_age_gender(): # 연령및 성별 브랜드 선호도 분석
    cloth_dict = {"상의" : "001",
                  "아우터": "002",
                  "하의": "003"}
    f = open('rank_age_gender.csv', 'w')
    csv_rank_age_gender = csv.writer(f)
    csv_rank_age_gender.writerow(['category', 'rank_brand_name', '~18', '19~23', '24~28', '29~33', '34~39', '40~', 'men', 'women'])
    for cloth in cloth_dict.keys():
        time.sleep(0.1)
        for i in range(1, 11): # 기존의 9000개 * 3(상의 하의 아우터) 데이터는 시간이 오래걸림 (1000개 데이터 기준 : 3시간 * 3)
            driver.get(f'https://www.musinsa.com/ranking/best?period=now&age=ALL&mainCategory={cloth_dict[cloth]}&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page={i}&viewType=small&priceMin=&priceMax=')
            for j in range(1, 91):
                driver.find_element_by_xpath(f'//*[@id="goodsRankList"]/li[{j}]/div[3]/div[1]/a').click()
                time.sleep(1)
                try:
                    brand_name = driver.find_element_by_css_selector(f'#wrap_rel_product > div.list-box.box.list_related_product.owl-carousel.owl-theme > div.owl-wrapper-outer > div > div.owl-item.active > ul > li:nth-child(1) > div.li_inner > div.article_info > p.item_title > a')
                    age_18 = driver.find_element_by_css_selector(f'#page_product_detail > div.right_area.page_detail_product > div.section_graph_detail > div > div > div.graph_bar_wrap > div > ul > li:nth-child(1) > dl > dd > p > span > span')
                    age_19_23 = driver.find_element_by_css_selector(f'#page_product_detail > div.right_area.page_detail_product > div.section_graph_detail > div > div > div.graph_bar_wrap > div > ul > li:nth-child(2) > dl > dd > p > span > span')
                    age_24_28 = driver.find_element_by_css_selector(f'#page_product_detail > div.right_area.page_detail_product > div.section_graph_detail > div > div > div.graph_bar_wrap > div > ul > li:nth-child(3) > dl > dd > p > span > span')
                    age_29_33 = driver.find_element_by_css_selector(f'#page_product_detail > div.right_area.page_detail_product > div.section_graph_detail > div > div > div.graph_bar_wrap > div > ul > li:nth-child(4) > dl > dd > p > span > span')
                    age_34_39 = driver.find_element_by_css_selector(f'#page_product_detail > div.right_area.page_detail_product > div.section_graph_detail > div > div > div.graph_bar_wrap > div > ul > li:nth-child(5) > dl > dd > p > span > span')
                    age_40 = driver.find_element_by_css_selector(f'#page_product_detail > div.right_area.page_detail_product > div.section_graph_detail > div > div > div.graph_bar_wrap > div > ul > li:nth-child(6) > dl > dd > p > span > span')
                    men =  driver.find_element_by_css_selector(f'#graph_doughnut_label > ul > li:nth-child(1) > dl > dd') # 추후 남성에게 가장 인기있는 브랜드 선정
                    women = driver.find_element_by_css_selector(f'#graph_doughnut_label > ul > li:nth-child(2) > dl > dd') # 추후 여성에게 가장 인기있는 브랜드 선정
                    csv_rank_age_gender.writerow([cloth, brand_name.text, age_18.text, age_19_23.text, age_24_28.text, age_29_33.text, age_34_39.text, age_40.text, men.text, women.text])
                    # time.sleep(0.5)
                    driver.back()
                    # time.sleep(0.5)
                except NoSuchElementException:
                    driver.back() # 순위에 분석에 필요한 연령 또는 성별이 없으면 건너뛴다.
                    # time.sleep(0.5) 
    driver.quit()

def reviews(): # 스타일 리뷰 (그냥 댓글의 경우 악성이 있을 수 있으므로 사진이 있는 것만) 뷴석 (판매 전략)
    cloth_dict = {# "상의" : "001",
                  "아우터": "002",
                  "하의": "003"}
    f = open('reviews2.csv', 'w') # 3만 다
    reviews = csv.writer(f)
    reviews.writerow(['category', 'review_type', 'rating', 'consumer', 'consumer rating', 'brand_name', 'review'])
    for cloth in cloth_dict.keys():
        time.sleep(0.1)
        for i in range(1, 11): # 기존의 9000개 * 3(상의 하의 아우터) 데이터는 시간이 오래걸림 (1000개 데이터 기준 : 3시간 * 3)
            driver.get(f'https://www.musinsa.com/ranking/best?period=now&age=ALL&mainCategory={cloth_dict[cloth]}&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page={i}&viewType=small&priceMin=&priceMax=')
            time.sleep(1)
            for j in range(1, 91):
                try:
                    driver.find_element_by_xpath(f'//*[@id="goodsRankList"]/li[{j}]/div[3]/div[1]/a').click()
                    time.sleep(1)
                    try:
                        driver.find_element_by_xpath(f'//*[@id="reviewSelectSort"]/option[5]').click()
                        time.sleep(1)
                        for i in range(1, 11):
                            brand_name = driver.find_element_by_css_selector(f'#wrap_rel_product > div.list-box.box.list_related_product.owl-carousel.owl-theme > div.owl-wrapper-outer > div > div.owl-item.active > ul > li:nth-child(1) > div.li_inner > div.article_info > p.item_title > a')
                            review = driver.find_element_by_css_selector(f'#reviewListFragment > div:nth-child({i}) > div.review-contents > div.review-contents__text')
                            rating = driver.find_element_by_css_selector(f'#estimate_point > p > span') # 해당 상품의 평균 구매 만족도
                            consumer = driver.find_element_by_css_selector(f'#reviewListFragment > div:nth-child({i}) > div.review-list__rating-wrap > span > span > span') # 구매자가 준 구매 만족도
                            consumer_information = driver.find_element_by_css_selector(f'#reviewListFragment > div:nth-child({i}) > div.review-profile > div > div.review-profile__information > p')
                            reviews.writerow([cloth, "낮은 평점", rating.text, consumer_information.text, consumer.get_attribute('style').split()[1], brand_name.text, review.text])
                        driver.find_element_by_xpath(f'//*[@id="reviewSelectSort"]/option[4]').click()
                        time.sleep(1)
                        for h in range(1, 11):
                            brand_name = driver.find_element_by_css_selector(f'#wrap_rel_product > div.list-box.box.list_related_product.owl-carousel.owl-theme > div.owl-wrapper-outer > div > div.owl-item.active > ul > li:nth-child(1) > div.li_inner > div.article_info > p.item_title > a')
                            review = driver.find_element_by_css_selector(f'#reviewListFragment > div:nth-child({h}) > div.review-contents > div.review-contents__text')
                            rating = driver.find_element_by_css_selector(f'#estimate_point > p > span') # 해당 상품의 평균 구매 만족도
                            consumer_information = driver.find_element_by_css_selector(f'#reviewListFragment > div:nth-child({i}) > div.review-profile > div > div.review-profile__information > p')
                            consumer = driver.find_element_by_css_selector(f'#reviewListFragment > div:nth-child({i}) > div.review-list__rating-wrap > span > span > span') # 구매자가 준 구매 만족도
                            reviews.writerow([cloth, "높은 평점", rating.text, consumer_information.text, consumer.get_attribute('style').split()[1], brand_name.text, review.text])
                        driver.back()
                        time.sleep(2)
                    except NoSuchElementException:
                        driver.back()
                        time.sleep(2)
                except:
                    pass
    driver.quit()



# reviews() # 의류에 대한 리뷰정보 분석
# top_brands() # 상위 9000등까지 랭크한 아이템 브랜드
# popular_items() # 인기 항목 / 무신사가 추천하는 아이템의 1000개의 브랜드
# rank_age_gender() # 연령및 성별 브랜드 선호도 분석
