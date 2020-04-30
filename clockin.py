from selenium.webdriver import Firefox
import time
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
f = open('number.txt', mode="a+", encoding="utf-8")
f.seek(0)
a = f.readline()
b = f.readline()

if (len(a.strip()) == 10):
    idnumber = a
    passwordnumber = b
else:

    idnumber = input("请输入您的学号: ")
    passwordnumber = input("请输入您的密码: ")
    f.seek(0)
    f.truncate()
    f.write(idnumber)
    f.write('\n')
    f.write(passwordnumber)
    f.write('\n')

f.close()
web = Firefox()

web.get("https://id.tsinghua.edu.cn/do/off/ui/auth/login/form/a585295b8da408afdda9979801383d0c/0?/fp/view?m=fp#act=fp/formHome")
wait = ui.WebDriverWait(web, 20)
wait.until(lambda driver: web.find_element_by_xpath('//*[@id="i_user"]'))
# 输入账号密码
web.find_element_by_xpath(
    '//*[@id="i_user"]').click()
id = web.find_element_by_xpath(
    '//*[@id="i_user"]')
id.send_keys('%s' % idnumber)
password = web.find_element_by_xpath(
    '//*[@id="i_pass"]')
password.send_keys('%s' % passwordnumber)


# 登录按钮
while web.find_element_by_xpath(
        "/html/body/div/div[2]/div/form/div[4]/a").is_enabled() == False:
    pass
web.find_element_by_xpath(
    "/html/body/div/div[2]/div/form/div[4]/a").click()

# 进入打卡
wait = ui.WebDriverWait(web, 20)
wait.until(lambda driver: web.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div[8]/div/div[1]/div/div/div/div[2]/div[6]/div[1]/div[3]"))
web.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div[8]/div/div[1]/div/div/div/div[2]/div[6]/div[1]/div[3]").click()

while 1:
    try:
        wait = ui.WebDriverWait(web, 10)
        wait.until(lambda driver: web.find_element_by_xpath(
            '//*[@id="commit"]'))
        time.sleep(4)
        web.find_element_by_xpath(
            '//*[@id="commit"]').click()
    except:
        break
web.quit()
print("打卡成功啦!")
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
