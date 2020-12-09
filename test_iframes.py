from selenium import webdriver
import pytest

def test_iframe():
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe')
    # 设置页面加载时间为5秒
    driver.set_page_load_timeout(5)
    driver.implicitly_wait(3)
    while True:
        try:
            driver.get('http://sahitest.com/demo/iframesTest.htm')
            break
        except:
            print('重新加载')
            pass

    driver.find_element_by_id('checkRecord').send_keys('999')
    driver.find_element_by_xpath('//input[@type="button"]').click()
    print(driver.find_element_by_id('checkRecord').text)

    # 进入第一个iframe中
    driver.switch_to.frame(0)
    assert 'http://sahitest.com/demo/linkTest.htm' == driver.find_element_by_link_text('Link Test').get_attribute('href')

    # 返回主界面
    driver.switch_to.default_content()

    # 进入第二个iframe中
    driver.switch_to.frame(driver.find_element_by_xpath('//div[@id="another"]/iframe'))
    assert 'http://sahitest.com/demo/jsPopup.htm' == driver.find_element_by_link_text('Js Popup').get_attribute('href')

    driver.quit()

if __name__ == '__main__':
    pytest.main()
