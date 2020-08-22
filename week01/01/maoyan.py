#引入需要的库
import pandas
import requests
from bs4 import BeautifulSoup as bs

#声明需要的变量
#待访问的网址
url = "https://maoyan.com/films?showType=3"
#电影字典数据初始化
movies_dict = {'title':[], 'category':[], 'release_date':[]}
#模拟请求headers
headers = { 
            'Host': 'maoyan.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'none',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer':url,
            'Cookie': '__mta=145119755.1597951624621.1597951832048.1597968882947.11;uuid_n_v=v1;uuid=1FE317A0E31B11EA81094F6760C63F1404B9C904DFB141D69A8E815BB91E71A3;_csrf=ce9e1ac3aa77524fcbaee9b1d790049e6c94f2e5dff31edb06c151f97449586d;Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597951624;_lxsdk_cuid=1740d56c400c8-03b0d8b29fb701-3c634103-144000-1740d56c400c8;_lxsdk=1FE317A0E31B11EA81094F6760C63F1404B9C904DFB141D69A8E815BB91E71A3;mojo-uuid=42412ee94402d1afd8f9483de31447f3;mojo-session-id={"id":"ec4861c411b42020c39e921802d37fc7","time":1598102799891};mojo-trace-id=3;Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598102906;__mta=145119755.1597951624621.1597968882947.1598102905871.12;_lxsdk_s=17416598281-232-cd0-46b%7C%7C7'
            }

#获取网页源代码
response = requests.session().get(url, headers=headers)
response.encoding='utf-8'
print(f'返回状态码:{response.status_code}')

#处理并输出文件保存
htmlparser = bs(response.text, 'html.parser')
for movies in htmlparser.find_all('div', attrs={"class": "movie-hover-info"}, limit=10):
    items = movies.find_all('div', attrs={'class': 'movie-hover-title'})
    movies_dict['title'].append(items[0].find('span',attrs={'class':'name'}).text.strip())
    movies_dict['category'].append(items[1].text.split(':')[1].strip())
    movies_dict['release_date'].append(items[3].text.split(':')[1].strip())
print(f'得到的电影信息:{movies_dict}')

#将电影信息保存到当前目录下movies.csv文件
df = pandas.DataFrame(data=movies_dict)
df.index = range(1,len(df)+1)
df.to_csv('./movies.csv', encoding='utf8')
