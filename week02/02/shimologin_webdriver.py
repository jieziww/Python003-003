from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
try:
    browser.get('https://shimo.im/login?from=home')
    sleep(2)
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('13999714382')
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('rj12345')
    browser.find_element_by_xpath('//button[text()="立即登录"]').click()
    print(browser.get_cookies())
    sleep(30) # 有时候弹出汉字的点击验证，需要人工操作
    print(browser.get_cookies())
except Exception as e:
    print(e)
finally:
    browser.close()


"""
[{'domain': '.shimo.im', 'httpOnly': False, 'name': 'Hm_lpvt_aa63454d48fc9cc8b5bc33dbd7f35f69', 'path': '/', 'secure': False, 'value': '1598800287'}, {'domain': '.shimo.im', 'expiry': 1630336286, 'httpOnly': False, 'name': 'Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69', 'path': '/', 'secure': False, 'value': '1598800287'}, {'domain': '.shimo.im', 'httpOnly': False, 'name': 'sensorsdata2015session', 'path': '/', 'secure': False, 'value': '%7B%7D'}, {'domain': '.shimo.im', 'expiry': 7906000286, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%221743fec526463-0b1a4d4d6cc068-3c634103-1327104-1743fec52659e8%22%2C%22%24device_id%22%3A%221743fec526463-0b1a4d4d6cc068-3c634103-1327104-1743fec52659e8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D'}, {'domain': '.shimo.im', 'expiry': 1598803885, 'httpOnly': True, 'name': 'shimo_sid', 'path': '/', 'secure': False, 'value': 's%3Azt1D2SD46Wk3WzoloCn4hRXIKax94g1d.isIL1bFp2xbxm7j4xITz8Rxj5QVBEbMPSA7VaqdTesU'}, {'domain': '.shimo.im', 'httpOnly': False, 'name': 'anonymousUser', 'path': '/', 'secure': False, 'value': '-10768247699'}, {'domain': 'shimo.im', 'httpOnly': False, 'name': '_csrf', 'path': '/', 'secure': False, 'value': 'O6TEr5X-jrnKs3HL-TakddSH'}, {'domain': '.shimo.im', 'expiry': 1914041420, 'httpOnly': False, 'name': 'shimo_svc_edit', 'path': '/', 'secure': False, 'value': '3961'}, {'domain': '.shimo.im', 'expiry': 1914333085, 'httpOnly': False, 'name': 'shimo_gatedlaunch', 'path': '/', 'secure': False, 'value': '2'}, {'domain': '.shimo.im', 'expiry': 1598803199, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.shimo.im', 'expiry': 1914333085, 'httpOnly': False, 'name': 'shimo_kong', 'path': '/', 'secure': False, 'value': '2'}, {'domain': '.shimo.im', 'httpOnly': False, 'name': 'deviceIdGenerateTime', 'path': '/', 'secure': False, 'value': '1598800285299'}, {'domain': '.shimo.im', 'httpOnly': False, 'name': 'deviceId', 'path': '/', 'secure': False, 'value': '4b4945f2-883b-4a1a-90fd-8caf52fd195f'}]
"""

"""
[{'domain': '.shimo.im', 'expiry': 7906000305, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%2246436318%22%2C%22%24device_id%22%3A%221743fec526463-0b1a4d4d6cc068-3c634103-1327104-1743fec52659e8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221743fec526463-0b1a4d4d6cc068-3c634103-1327104-1743fec52659e8%22%7D'}, {'domain': '.shimo.im', 'httpOnly': False, 'name': 'Hm_lpvt_aa63454d48fc9cc8b5bc33dbd7f35f69', 'path': '/', 'secure': False, 'value': '1598800287'}, {'domain': '.shimo.im', 'httpOnly': False, 'name': 'sensorsdata2015session', 'path': '/', 'secure': False, 'value': '%7B%7D'}, {'domain': '.shimo.im', 'expiry': 1598803885, 'httpOnly': True, 'name': 'shimo_sid', 'path': '/', 'secure': False, 'value': 's%3Azt1D2SD46Wk3WzoloCn4hRXIKax94g1d.isIL1bFp2xbxm7j4xITz8Rxj5QVBEbMPSA7VaqdTesU'}, {'domain': '.shimo.im', 'httpOnly': False, 'name': 'anonymousUser', 'path': '/', 'secure': False, 'value': '-10768247699'}, {'domain': 'shimo.im', 'httpOnly': False, 'name': '_csrf', 'path': '/', 'secure': False, 'value': 'O6TEr5X-jrnKs3HL-TakddSH'}, {'domain': '.shimo.im', 'expiry': 1914041420, 'httpOnly': False, 'name': 'shimo_svc_edit', 'path': '/', 'secure': False, 'value': '3961'}, {'domain': '.shimo.im', 'expiry': 1914333104, 'httpOnly': False, 'name': 'shimo_gatedlaunch', 'path': '/', 'secure': False, 'value': '2'}, {'domain': '.shimo.im', 'expiry': 1598803199, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.shimo.im', 'expiry': 1914333085, 'httpOnly': False, 'name': 'shimo_kong', 'path': '/', 'secure': False, 'value': '2'}, {'domain': '.shimo.im', 'expiry': 1630336286, 'httpOnly': False, 'name': 'Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69', 'path': '/', 'secure': False, 'value': '1598800287'}, {'domain': '.shimo.im', 'httpOnly': False, 'name': 'deviceIdGenerateTime', 'path': '/', 'secure': False, 'value': '1598800285299'}, {'domain': 'shimo.im', 'expiry': 1614352306, 'httpOnly': False, 'name': '_bl_uid', 'path': '/', 'secure': False, 'value': '73k16etRhkF8bhfb67LpwF33OsgO'}, {'domain': '.shimo.im', 'httpOnly': False, 'name': 'deviceId', 'path': '/', 'secure': False, 'value': '4b4945f2-883b-4a1a-90fd-8caf52fd195f'}]
"""
