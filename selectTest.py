from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe')
driver.get('http://sahitest.com/demo/selectTest.htm')

# 第一个选择框
for i in range(1,4):
    driver.find_element_by_id('id'+str(i)).click()
    sleep(0.5)

# 第二个选择框
select2 = Select(driver.find_element_by_id('s2Id'))
for i in range(1,4):
    select2.select_by_index(i)
    sleep(0.5)

# 第三个选择框
select3 = Select(driver.find_element_by_id('s3Id'))
for i in range(1,4):
    select3.select_by_visible_text('o'+str(i))


# 第四个多选框
select4 = Select(driver.find_element_by_id('s4Id'))
for i in range(1,5):
    select4.select_by_value('o'+str(i)+'val')


# 第五个选择框
select5 = Select(driver.find_element_by_id('s1'))
for i in range(46,52):
    select5.select_by_value(str(i))

sleep(5)
quit()