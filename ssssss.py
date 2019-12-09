import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
url = "https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1564323412623"
u = "https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D"
a = requests.get(url).text
print(a)
with open("1.html","a+") as f:
    f.write(a)
