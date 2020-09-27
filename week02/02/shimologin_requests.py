from fake_useragent import UserAgent
from time import sleep
import requests
import json

user_agent = UserAgent(verify_ssl=False)
headers = {
  'User-Agent': user_agent.chrome,
  'Referer': 'https://shimo.im/login?from=home',
  'X-Requested-With' : 'XmlHttpRequest',    # ajax 提交
  'x-source' : 'lizard-desktop'
}

index_url = "https://shimo.im/welcome"

login_url = 'https://shimo.im/lizard-api/auth/password/login'
captcha_url = 'https://shimo.im/lizard-api/auth/geetest/captcha?scene=web_login'

s = requests.Session()
s.get(index_url, headers=headers) # 得到cookies

sleep(3)


post_data = {
    'geetest_challenge':'5d080b2ea38bac7b6bdf8319d6f1af05',
    'geetest_validate':'98e2e1e27e364c20829ef70afa06598e',
    'geetest_seccode':'98e2e1e27e364c20829ef70afa06598e|Cjordan',
    'mobile': '+8613999714382',
    'password': 'rj12345'
    }

response = s.post(login_url, data=post_data, headers=headers)
# 有个比较变态的汉字点击认证，感觉还没有到达那一步，本周没有时间，不死磕了。
print(response.text)
print(response.status_code)
