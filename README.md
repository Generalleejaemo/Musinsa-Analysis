# <center> Musinsa data Analysis </center>
<img src = "https://user-images.githubusercontent.com/75519839/172176646-213c370f-13b5-4efd-924c-08bb4ad3fa7c.png" width = "700px"></img>

Extract Data From Musinsa Using Selenium & Selenium/Python
<img src = "https://user-images.githubusercontent.com/75519839/153009836-fc8e76bd-754c-4061-81c8-7a3a396b8144.png" width="30px">
Link: [Musinsa](https://www.musinsa.com/app/)

***
### Install
<pre><code>pip install -r requirements.txt</code></pre>
해당 파일은 Python 3.8 버젼에서 제작되었습니다. 🧐
***

### System Architecture

![Project_musinsa](https://user-images.githubusercontent.com/75519839/166198654-f02eb5a3-8936-46b7-90e4-69840c8d13e5.png)

## 1. 프로젝트 소개 🚀

- 해당 프로젝트는 무신사 사이트를 기반으로 제작되었습니다.
- 평소에 관심이 많았던 이커머스 플랫폼인 무신사에 대해 알고 싶었던 정보를 수집하고 분석해보았습니다.
- 분석된 데이터를 기반으로 직관적인 정보를 제공하는 서비스를 기획하였습니다.

## 2. 제작 과정 및 가설 수립 🌿

<img width="1060" alt="image" src="https://user-images.githubusercontent.com/75519839/166198739-210067cc-68e8-4d2f-9d9f-cc2b173a0479.png">

- 소비자 댓글 데이터를 통해 불만사항 또는 선호사항을 조사하여 상품들의 공통 개선사항을 무엇인가?
- 랭킹 데이터를 재분석하여 현재 무신사의 중심 브랜드와 가장 트렌디한 브랜드는 무엇인가?
- 상품의 이미지로 사용하기에 가장 좋은 색상은 무엇인가?
- 상품의 이름으로 가장 적합한 것은 무엇인가? (소비자의 시선을 끌만한 이름)
- 실시간 검색에 자주 등장하는 상품과 현재 진행중인 이벤트와의 연관성은 어느정도 인가?

## 3. 분석 시각화 🔍
### Metabase를 통해 시각화하였습니다.

- 해딩 링크를 통해서 자세한 내용을 확인해보실 수 있습니다.
[✅](https://github.com/godhin/Musinsa-Analysis/files/8845368/Dashboard.Metabase.pdf)


![image](https://user-images.githubusercontent.com/75519839/172188358-3010b4a8-3f2d-4b16-afcd-55bb8e75970d.png)
![image](https://user-images.githubusercontent.com/75519839/172188429-5278fdee-750a-483c-8771-5964b3bb25df.png)
![image](https://user-images.githubusercontent.com/75519839/172188463-0270c80e-99cd-4172-96e8-98d8d7f09a0c.png)



## 4. 가설검정 결과 및 실패 원인 분석 ⭐️

- Q. 소비자 댓글 데이터를 통해 불만사항 또는 선호사항을 조사하여 상품들의 공통 개선사항을 무엇인가?
  - ![good_text](https://user-images.githubusercontent.com/75519839/172188848-13f9e001-f18e-4143-becc-dada43b3109e.jpg)
  - ![bad_text](https://user-images.githubusercontent.com/75519839/172188836-41594547-514b-4a84-a27e-5a148c51a5fd.jpg)
    - A-1. 간단한 워크클라우드를 구현해보았습니다. 전체적으로 고객이 선호하는 핏과 기장이 다른 경우 불만을 보였습니다.
    - A-2. 무신사에서 제공하는 사이즈표와 맞게 기장을 수정하거나, 해당 상품의 상세설명을 추가하는 방향으로 문제를 해결할 수도 있을 것 같습니다.
- Q. 랭킹 데이터를 재분석하여 현재 무신사의 중심 브랜드와 가장 트렌디한 브랜드는 무엇인가?
  - A-남성. 브랜디드
  - A-여성. 네스티팬시클럽
  - A-10대 : 커버낫
  - A-20대 초 : 스컬프터
  - A-20대 중후반 : 인사일런스
  - A-30대 초 : 무신사 스탠다드
  - A-30대 중후반 : 무신사 스탠다드
  - A-40대 이후 : 와릿이즌
    - ![image](https://user-images.githubusercontent.com/75519839/172189967-3eb85cad-cad3-4f1e-8ad3-873dfcd2ad74.png)
    - A. 전체적으로 자사 브랜드인 무신사 스탠다드의 비율이 높았으며 인기또한 우세했습니다. 좋은 품질과 가성비가 가장 큰 몫을 하였으며, 소비자가 선호하는 사항에 가장 적합한 상품이였습니다.

- Q. 상품의 이미지로 사용하기에 가장 좋은 색상은 무엇인가?
  - A. 상품과 연관이 없는 사진인 경우가 많아서 분석에서 제외하였습니다.
    - 원인 분석 🫥
    - 신발이나 바지 사진에 모델 전체가 등장하는 경우가 많았음
    - 해당 분석은 바지일 경우 바지만 찾는 인식 모델을 만든 이후 모델을 기반으로 바지인 부분만 색상추출하여 진행하여야 할 것으로 보임 (다른 카테고리도 마찬가지)
- Q. 상품의 이름으로 가장 적합한 것은 무엇인가? (소비자의 시선을 끌만한 이름)
  - A. 이름에 상품 고유 코드 ex) J216047 1AA 가 포함되어 있는 경우가 다부해서 분석 불가로 판단
    - 원인 분석 🫥
    - 고유 코드가 들어간 경우 전처리가 복잡해지기에 프로젝트의 방향성과 시간적으로 보았을 때 비효율적임
- Q. 실시간 검색에 자주 등장하는 상품과 현재 진행중인 이벤트와의 연관성은 어느정도 인가?
  - 분석 실패
    - 원인 분석 🫥
    - 실시간 데이터를 이벤트 기간동안 수집 가능한 양이 적기때문에 보다 정확한 결과를 얻지 못할 것으로 판단
    - 일주일 정도 분석해본 결과 특정 이벤트가 열릴 경우 해당 이벤트와 연관된 브랜드가 검색어에 올라오긴 함

## 5. 서비스 구현
- 최소한의 기능만 구현후 현재 구현중

## 추가 ++. 리뷰 분석

![image](https://user-images.githubusercontent.com/75519839/172191597-2e3ae21d-904d-45d0-997a-08277e07bdd6.png)

- 수집한 리뷰 데이터 (평점 기반)을 통해 모델 학습 후 리뷰가 부정적인지 긍정적인지 추가 분석
- 실시간 리뷰 데이터를 기반으로 해당 리뷰가 긍정인지 부정인지 분석

### 도출할 수 있는 결과 😈
- 평점과 별개로 리뷰를 적는 글들을 판별하여 실질적인 부정 리뷰와 긍정 리뷰를 판별할 수 있음
- 부정적인 리뷰중 높은 평점을 주는 리뷰는 비판적인 경우가 많기에 구매전 참고할 수 있음


