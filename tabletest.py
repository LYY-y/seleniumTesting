from selenium import webdriver
from selenium.webdriver.support.ui import Select
class table:
    '''
    find_elements...返回的是列表，所以索引从1开始！！！
    xpath中[n]表示第n个
    table中行、列值从1算起！！！
    '''

    def __init__(self,driver):
        self.driver = driver

    # 获取行、列值
    def get_table_row_and_col(self, table_locator):
        locator = '//%s/tbody' % (table_locator)
        row = len(self.driver.find_elements_by_xpath(locator+'/tr'))
        col = len(self.driver.find_elements_by_xpath(locator+'/tr[1]/td'))
        return row, col

    # 根据行列获取文本值(包含标题)
    def get_table_text_by_row_and_col(self, table_locator, row, col):
        locator = '//%s/tbody/tr[%s]/td[%s]' % (table_locator, row, col)
        text = self.driver.find_element_by_xpath(locator).text
        return text


if __name__ == '__main__':
    driver = webdriver.Chrome("F:\chromedriver_win32\chromedriver.exe")
    driver.get("http://sahitest.com/demo/tableTest.htm")
    driver.implicitly_wait(10)
    table = table(driver)
    # 遍历第一个table的元素 Table Without Id
    print('第一个table')
    table_locator = 'table[1]'
    row, col = table.get_table_row_and_col(table_locator)
    for i in range(1, row+1):
        for j in range(1, col+1):
            print(table.get_table_text_by_row_and_col(table_locator,i,j), end=' ')
        print()

    # 遍历第二个table的元素 Cell By Row Column
    print('第二个table')
    table_locator = 'table[@id="t2"]'
    row, col = table.get_table_row_and_col(table_locator)
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print(table.get_table_text_by_row_and_col(table_locator, i, j), end=' ')
        print()

    # 遍历第三个table的元素 Table With Id
    print('第三个table')
    # html中有两处id值为tableWithId，取第一个
    table_locator = 'table[@id="tableWithId"][1]'
    row, col = table.get_table_row_and_col(table_locator)
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print(table.get_table_text_by_row_and_col(table_locator, i, j), end=' ')
        print()

    # 遍历第四个table的元素
    print('第四个table')
    table_locator = 'table[4]'
    row, col = table.get_table_row_and_col(table_locator)
    for i in range(1, row + 1):
        locator = ('//'+table_locator+ '/tbody/tr[' + str(i) + ']')
        for j in range(1, col + 1):
            # 图片img
            if j == 1:
                print(driver.find_element_by_xpath(locator+'/td[1]/img').get_attribute('src'),end=' ')
            # 文本框textarea
            if j == 2:
                d = driver.find_element_by_xpath(locator+'/td[2]/textarea')
                d.clear()
                d.send_keys('999')
                print(driver.find_element_by_xpath(locator+'/td[2]/textarea').text,end=' ')
            # 文本
            if j == 3:
                print(driver.find_element_by_xpath(locator + '/td[3]').text,end=' ')
            # 链接
            if j == 4:
                driver.find_element_by_xpath(locator + '/td[4]/a[1]').click()
                driver.back()
                driver.find_element_by_xpath(locator + '/td[4]/a[2]').click()
                driver.back()
                print(driver.find_element_by_xpath(locator +'/td[4]').text,end=' ')
            # input[type='checkbox']
            if j == 5:
                driver.find_elements_by_name('cb')[i-1].click()
            # input[type='textbox']
            if j == 6:
                driver.find_elements_by_name('tb')[i-1].send_keys('753')
            # input[type='password']
            if j == 7:
                driver.find_elements_by_name('pwd')[i-1].send_keys('888')
            # input[type='radio']
            if j == 8:
                driver.find_elements_by_name('rad')[i-1].click()
            # input[type='button']
            if j == 9:
                driver.find_elements_by_name('btn')[i-1].click()
            # input[type='submit']
            if j == 10:
                driver.find_elements_by_name('sbmt')[i-1].click()
            # input[type='image']
            if j == 11:
                print(driver.find_elements_by_name('img_sbmt')[i-1].get_attribute('src'),end=' ')
                print(driver.find_element_by_xpath(locator+'/td[11]/span').text,end=' ')
        print()

    # 遍历第五个table的元素 Table With thead and tbody
    print('第五个table')
    table_locator = 'table[@id="tableWithId"][2]'
    row, col = table.get_table_row_and_col(table_locator)
    # 输出caption
    print(driver.find_element_by_tag_name('caption'))
    # 输出thead
    print(driver.find_element_by_tag_name('thead'))
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print(table.get_table_text_by_row_and_col(table_locator, i, j), end=' ')
        print()

    # 遍历第六个table的元素 Cell with new line for array comparison check.
    print('第六个table')
    table_locator = 'table[@id="t3"]'
    row, col = table.get_table_row_and_col(table_locator)
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print(table.get_table_text_by_row_and_col(table_locator, i, j), end=' ')
        print()

    # 遍历第七个table的元素 Employment Detail Table
    print('第七个table')
    table_locator = 'table[@id="t4"]'
    row, col = table.get_table_row_and_col(table_locator)
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print(table.get_table_text_by_row_and_col(table_locator, i, j), end=' ')
        print()

    # 遍历第八个table元素
    print('第八个table')
    select = Select(driver.find_element_by_id('s1'))
    select.select_by_index(1)
    select.select_by_index(0)
    print(driver.find_element_by_id('cell2'))

    quit()