from selenium import webdriver
import time
import pymysql


try:
    browser = webdriver.Chrome()
    browser.get('https://www.douban.com')
    time.sleep(1)
    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()
    browser.find_element_by_xpath('//*[@id="username"]').send_keys('')
    browser.find_element_by_id('password').send_keys('')
    time.sleep(1)
    browser.find_element_by_xpath(
        '//a[contains(@class,"btn-account")]').click()
    time.sleep(5)

    db = pymysql.connect("localhost", "root", "rj123", "douban")
    cursor = db.cursor()

    rating_dict = {'力荐': 5, '推荐': 4, '还行': 3, '较差': 2, '很差': 1}

    for id in range(0, 100, 20):
        browser.get(
            f'https://movie.douban.com/subject/1292052/comments?start={id}&limit=20&status=P&sort=new_score')
        comments = browser.find_elements_by_class_name("comment")
        for comment in comments:
            useful = comment.find_element_by_class_name("vote-count")
            username = comment.find_elements_by_tag_name("a")
            rating = comment.find_element_by_class_name("rating")
            time = comment.find_element_by_class_name("comment-time")
            content = comment.find_element_by_class_name("comment-content")

            sql = f"""insert into shawshank(useful,username, rating, time, content) values ({useful.text}, '{username[1].text}', {rating_dict[rating.get_attribute("title")]}, '{time.text}', '{content.text}')"""
            print(sql)
            try:
                cursor.execute(sql)
                db.commit()
            except Exception:
                db.rollback()
    db.close()
except Exception as e:
    print(e)
finally:
    browser.close()
