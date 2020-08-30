from fake_useragent import UserAgent
from time import sleep
import requests
import json

user_agent = UserAgent()
headers = {
  'User-Agent': user_agent.chrome,
  'Referer': 'https://shimo.im/login?from=home'
}

index_url = "https://shimo.im/welcome"

# 通过故意录入错误密码获得api地址，反馈的是json数据。
login_url = 'https://shimo.im/lizard-api/auth/password/login'

s = requests.Session()
s.get(index_url, headers=headers) # 得到cookies

sleep(3)

# 这个数据提交后403，而且提交json格式也不行
post_data = {
  'mobile': '+8613999714382',
  'password': 'rj12345'
  }

response = s.post(login_url, data=post_data, headers=headers)

# 返回信息如下面的情况，403
# 无法获取有效的登录信息，后期有时间了仔细分析一下报文。可能不是直接这样post这么简单。
# 而且即使登录成功，有个比较变态的汉字点击认证，感觉还没有到达那一步，本周没有时间，不死磕了。
# 后面有时间了，最起码做到可以得到跳转到汉字点击认证界面的链接。

print(response.text)
# 大部分运行显示这个提示
#CSRF violation

# 有时候显示如下信息
#<html>
#<head><title>403 Forbidden</title></head>
#<body>
#<center><h1>403 Forbidden</h1></center>
#<hr><center>openresty/1.15.8.2</center>
#</body>
#</html>
#<!-- a padding to disable MSIE and Chrome friendly error page -->
#<!-- a padding to disable MSIE and Chrome friendly error page -->
#<!-- a padding to disable MSIE and Chrome friendly error page -->
#<!-- a padding to disable MSIE and Chrome friendly error page -->
#<!-- a padding to disable MSIE and Chrome friendly error page -->
#<!-- a padding to disable MSIE and Chrome friendly error page -->

print(response.status_code)
#403
