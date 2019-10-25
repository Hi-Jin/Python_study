import requests
from bs4 import BeautifulSoup as bs

# 사이버캠퍼스 주소 과목별로 올리기
lecture_url = {
    "http://e-learn.cnu.ac.kr/lms/class/classroom/doViewClassRoom_new.dunet",
    "http://e-learn.cnu.ac.kr/lms/class/classroom/doViewClassRoom_new.dunet"
}

# 사이버캠퍼스 아이디, 비밀번호
payload = {
    '_enpass_login_': 'submit',
    'userId': 'myID','s'
    'saveLoginID': 'checkbox',
    'password': 'myPW',
    'x': '0',
    'y': '0'
    # x, y 부분이 로그인시마다 변경되는데, 어떻게 x, y를 찾아서 로그인 해야하지..?
}


def crawling(_url):
    response = s.get(_url)
    response.raise_for_status()

    soup = bs(response.text, "html.parser")
    print(soup.get_text)


url = "http://portal.cnu.ac.kr"

s = requests.session()

res = s.post(url, data=payload)
res.raise_for_status()

for url in lecture_url:
    crawling(url)
    print("\n")
