from bs4 import BeautifulSoup
import requests
import re
import  pandas as pd
import  datetime

category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']
df_titles = pd.DataFrame()
for i in range(6):   #category 가 6라서 for문 돌림
    url = 'https://news.naver.com/section/10{}'.format(i)  # 문자열로 줘야함

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')  # 유니코드같은 읽을수 없는 코드등을 정리해주는 코드

    title_tags = soup.select('.sa_text_strong')  # 네이버 뉴스에서 보고 정의되어 있는대로 가져옴 sa 앞에 . 은 클래스임
# title = title_tags[0].text 첫번째 제목 하나 가져오기
# print(title)

    titles = []
    for tag in title_tags:
        titles.append(tag.text)
    print(titles)
    df_section_titles = pd.DataFrame(titles, columns=['titles'])
    df_section_titles['category'] = category[i]  # 카테고리 나타내는 코드
    df_titles = pd.concat([df_titles, df_section_titles],   #합치는코드
                      axis='rows', ignore_index=True)
print(df_titles.head())
df_titles.info()
print(df_titles['category'].value_counts()) # 카테고리 별로 몇개인지
df_titles.to_csv('./crawling_data/naver_headline_news_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index =False) # 폴더안에 넣는 코드