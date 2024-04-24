import requests

URL = "https://coopjbnu.kr/function/ajax.get.rest.data.php"

with open("./cafeteria_menu.html", "w", encoding="UTF-8") as f:
    res = requests.get(URL)
    res.encoding = "UTF-8"
    f.write(res.text)