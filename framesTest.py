from selenium import webdriver

driver = webdriver.Chrome("F:\chromedriver_win32\chromedriver.exe")
# 设置页面加载时间为5秒
driver.set_page_load_timeout(5)
while True:
    try:
        driver.get('http://www.sahitest.com/demo/framesTest.htm')
        break
    except:
        print('重新加载')
        pass

# 若无切入到frame直接定位会报错！
# print(driver.find_element_by_link_text('Link Test'))

# frame元素用name切入
driver.switch_to.frame('top')
print(driver.find_element_by_link_text('Link Test').get_attribute('href'))

# 执行操作下一个iframe时，需要先跳出当前iframe，以下两种方法均可
# 方法一：跳出所有iframe，回到主界面
# driver.switch_to.default_content()
# 方法二：返回上一级界面
driver.switch_to.parent_frame()

# 用frame的index来定位，第一个是0
driver.switch_to.frame(1)
print(driver.find_element_by_link_text('Js Popup').get_attribute('href'))

driver.quit()