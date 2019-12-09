import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
def sp(offest,keyword):
    data = {
        "aid": 24,
        "app_name": "web_search",
        "offset": offest,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": 20,
        "en_qc": 1,
        "cur_tab": 1,
        "from": "search_tab",
        "pd": "synthesis",
        "timestamp": 1564323412623

    }
    url = "https://www.toutiao.com/api/search/content/?" + urlencode(data)
    print(url)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    a = requests.get(url).text
    print(a)


if __name__ == "__main__":
    sad = sp(0,"街拍")


