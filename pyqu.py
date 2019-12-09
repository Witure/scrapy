from pyquery import PyQuery as pq
doc =pq("<p>sdadasd<p>") #解析html字符串
print(doc)
doe =pq("http://news.baidu.com/") #解析网页
# print(doe)
dof =pq("./a.html") #解析html 文本
print(dof)