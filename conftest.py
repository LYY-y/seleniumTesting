import pytest
from selenium import webdriver

@pytest.fixture(scope='module')
def connect():
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe')
    # 设置页面加载时间为5秒
    driver.set_page_load_timeout(5)
    driver.implicitly_wait(3)
    while True:
        try:
            driver.get('http://sahitest.com/demo/shadowRoot.html')
            print('成功连接')
            return driver
        except:
            print('重新加载')
            pass

