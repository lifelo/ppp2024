from bs4 import BeautifulSoup
import requests

def main():
    url = "https://ieilms.jbnu.ac.kr/weeklyLecture/index.jsp"
    resp = requests.get(url)
    soup =  BeautifulSoup(resp.text, 'html.parser')
    #print(soup.text)
    #print(soup.find("type06_headline"))
    #resp.encoding = "utf8"
    #print(resp.content)
    #print(soup.table.findall("td", "left"))
    for idx, news_item in enumerate(soup.table.find_all("td", "left")):
        print(f'{idx+1} - {news_item.a["title"]}')


if __name__ == "__main__":
    main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        