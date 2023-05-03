# # 크롬 드라이버 설치
# https://chromedriver.chromium.org/downloads

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip
import time

# id, pw 파일 불러오기
f = open("id파일 경로", 'r')
data = f.read()
f.close()
id, pw = data.split('\n')

# 브라우저 실행
driver = webdriver.Chrome() # 작동 안되면 chromedriver.exe 파일 경로 추가

# 네이버 이동
driver.get('http://naver.com')
time.sleep(0.5)

# 로그인 버튼 클릭
elem = driver.find_element_by_class_name('link_login')
elem.click()
time.sleep(1)

# id 복사 붙여넣기
elem_id = driver.find_element_by_id('id')
elem_id.click()
pyperclip.copy(id)
elem_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 복사 붙여넣기
elem_pw = driver.find_element_by_id('pw')
elem_pw.click()
pyperclip.copy(pw)
elem_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element_by_id('log.login').click()
time.sleep(0.5)

# 등록 안함 버튼 클릭
try:
    elem = driver.find_element_by_id('new.dontsave')
    elem.click()
    time.sleep(0.5)
except:
    pass

# 사전 페이지로 이동
driver.get('https://en.dict.naver.com/')
time.sleep(0.5)

# 검색창 클릭
elem = driver.find_element_by_id('ac_input')
elem.click()
time.sleep(0.5)

# 자동저장 활성화
elem = driver.find_element_by_class_name('label_add_auto')
elem.click()
time.sleep(1)

# 알람이 뜨면 확인
try:
    alart = driver.switch_to_alert()
    alart.accept()
except:
    print("there is no alert")
time.sleep(1)

# 단어장 파일 불러오기
f = open("단어장 파일 경로", 'r')
words = list(map(lambda s: s.strip(), f.readlines()))
f.close()

# 단어를 검색, 단어 뜻을 확인하면 자동으로 추가됨
for w in words:
    try:
        elem = driver.find_element_by_id('ac_input')
        elem.click()

        elem.send_keys(Keys.CONTROL, 'a')
        elem.send_keys(w)
        time.sleep(0.5)
        elem = driver.find_element_by_class_name('btn_search')
        elem.click()
        time.sleep(0.5)

        elem = driver.find_element_by_class_name('highlight')
        elem.click()
        time.sleep(0.5)
    except:
        print('word add error')

# 브라우저 종료
driver.quit()
