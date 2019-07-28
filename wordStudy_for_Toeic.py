while(True):
    word = input("모르는 단어(종료 = 0): ")
    if(word == "0"):
        print("수고하셨습니다.")
        break
    import requests
    from bs4 import BeautifulSoup

    url = "https://fraze.it/n_search.jsp?hardm=1&t=0&l=0&p=1&q=" + word # p == page_num

    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, "html.parser")

    for i in range(8):
        print(soup.find_all('div', class_='qu_txt')[i].text.replace("(open, save, copy)", ""))
