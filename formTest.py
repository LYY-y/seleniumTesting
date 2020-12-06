from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

def handleAcceptAlert(driver):
    driver.switch_to.alert.accept()

driver = webdriver.Chrome("F:\chromedriver_win32\chromedriver.exe")
driver.get("http://sahitest.com/demo/formTest.htm")

# 初始化页面有弹窗
driver.switch_to.alert.accept()
sleep(2)

# 根据name定位元素并输入值
driver.find_element_by_name("t1").send_keys("1")

# 根据xpath定位并输入值
driver.find_element_by_xpath("//tbody/tr[3]/td[2]/input").send_keys("2")

# 根据name=name定位元素并输入值
driver.find_element_by_name("name").send_keys("3")

# 根据name=$a_dollar定位元素
driver.find_element_by_name("$a_dollar").send_keys("4")

# 根据name定位disabled元素，输入值
try:
    driver.find_element_by_name("textdisabled").send_keys("5")
except:
    assert driver.find_element_by_name("textdisabled").get_attribute("value") == ''

# 根据name定位readonly元素，输入值
driver.find_element_by_name("textreadonly").send_keys("6")
assert driver.find_element_by_name("textreadonly").get_attribute("value") == ''

# 根据name定位textarea无效类型元素，输入值,可获取值但不是textarea
driver.find_element_by_name("invalidType").send_keys("7")
print('当input的type=textarea时，',driver.find_element_by_name("invalidType").get_attribute("value"))

# 根据name定位invalid无效类型元素，输入值,可获取值
driver.find_element_by_name("invalidType2").send_keys("8")
print('当input的type=invalid时，',driver.find_element_by_name("invalidType2").get_attribute("value"))

driver.find_element_by_name('noType').send_keys('9')

# 根据name定位textarea元素，并向textarea传入换行的字符串
js = 'document.getElementsByName("ta1")[0].innerHTML="123\\n456"'
driver.execute_script(js)
print('富文本框1的值：',driver.find_element_by_name('ta1').get_attribute('value'))

# 根据xpath定位textarea
driver.find_elements_by_tag_name("textarea")[2].send_keys("9")
print('富文本框2的值：',driver.find_elements_by_tag_name("textarea")[2].get_attribute('value'))

# 定位checkbox
checkbox = driver.find_elements_by_css_selector('input[type="checkbox"]')
# 全部选中
for check in checkbox:
    check.click()
# 检验是否全部选中
for check in checkbox:
    assert check.is_selected()
# 最一个选框不选
checkbox.pop().click()
# 第二个选框不选.pop(n)是返回当前选择的里面第n+1个元素（第一个元素为0）
checkbox.pop(1).click()
# 检验是否第二个和第四个未选中
assert driver.find_elements_by_css_selector('input[type="checkbox"]')[1].is_selected() == False
assert driver.find_elements_by_css_selector('input[type="checkbox"]')[3].is_selected() == False

# 定位radio
radio = driver.find_elements_by_css_selector('input[type="radio"]')
# 逐个点击radio
for r in radio:
    r.click()
# 确定radio当前选择的值未最后一个rv2
assert driver.find_elements_by_name('r1')[1].is_selected() == True

# 定位password并输入值
driver.find_element_by_name('p1').send_keys('abc')
assert driver.find_element_by_name('p1').get_attribute('value') == 'abc'
driver.find_elements_by_css_selector('input[type="password"]')[1].send_keys('def')
assert driver.find_elements_by_css_selector('input[type="password"]')[1].get_attribute('value') == 'def'

# 定位select元素
select = Select(driver.find_element_by_id('s1Id'))
# 根据选项的次序(从0开始），选择元素。
select.select_by_index(0)
sleep(1)
# 根据选项的value属性值，选择元素。
select.select_by_value('o2')
# 点击不同的选项发生弹窗
handleAcceptAlert(driver)
sleep(1)
# 根据选项的可见文本，选择元素。
select.select_by_visible_text('o3')
handleAcceptAlert(driver)
# 输出选择的文本应该为o3
print(select.all_selected_options[0].text)
assert select.all_selected_options[0].text == 'o3'
sleep(2)

select = Select(driver.find_elements_by_id('s1Id')[1])
# 根据选项的次序(从0开始），选择第3个元素。
select.select_by_index(2)
# 根据选项的value属性值，选择第2个元素。
select.select_by_value('o2')
# 根据选项的可见文本，选择元素。
select.select_by_visible_text('o3')
# 输出选择的文本应该为o3
assert select.all_selected_options[0].text == 'o3'
sleep(2)

select = Select(driver.find_elements_by_css_selector('select')[2])
# 根据选项的次序(从1开始），选择元素。
select.select_by_index(1)
# 根据选项的value属性值，选择元素。
select.select_by_value('o2')
# 根据选项的可见文本，选择元素。
select.select_by_visible_text('o3')
# 输出选择的文本应该为o3
assert select.all_selected_options[0].text == 'o3'

# select多选
select = Select(driver.find_elements_by_css_selector('select')[3])
for i in range(1,4):
    select.select_by_value('o'+str(i))
    handleAcceptAlert(driver)
# 输出已选择的选项
arr = []
selected = select.all_selected_options
for i in range(len(selected)):
    arr.append(selected[i].text)
print("多选框已选的内容：", arr)

# 点击input[type=button]
driver.find_element_by_id('btnId').click()
driver.find_elements_by_name('btnName')[1].click()
driver.find_elements_by_id('btnId')[2].click()
driver.find_elements_by_css_selector('input[type="button"]')[3].click()

# 点击input[type=reset]
driver.find_element_by_name('resetTest').send_keys('123')
driver.find_element_by_id('resetId').click()
driver.find_element_by_name('resetTest').send_keys('123')
driver.find_element_by_name('resetName').click()
driver.find_element_by_name('resetTest').send_keys('123')
driver.find_element_by_id('resetId1').click()
driver.find_element_by_name('resetTest').send_keys('123')
driver.find_element_by_xpath('//input[@type="reset"]').click()

# 点击button元素
driver.find_element_by_id('buttonId').click()
driver.find_element_by_xpath('//button[@type="submit"]').click()
handleAcceptAlert(driver)
driver.find_element_by_xpath('//button[@type="reset" and @id="buttonId"]').click()

# 点击input[type='submit']
driver.find_element_by_id('submitBtnId').click()
handleAcceptAlert(driver)
driver.find_elements_by_id('submitBtnId')[1].click()
handleAcceptAlert(driver)
driver.find_elements_by_id('submitBtnId')[2].click()
handleAcceptAlert(driver)
driver.find_elements_by_css_selector('input[type="submit"]')[3].click()
handleAcceptAlert(driver)



# 点击image元素
driver.find_element_by_id('imageId1').click()
driver.find_elements_by_id('imageId1')[1].click()
driver.find_elements_by_css_selector('img[src="add.gif"]')[2].click()

# 点击input[type=text]搜素
driver.find_element_by_id('q').send_keys('10')
assert driver.find_element_by_name('qs').get_attribute('alt') == 'Search'
driver.find_elements_by_xpath('//input[@type="image" and @name="qs"]')[1].click()
handleAcceptAlert(driver)
driver.find_element_by_xpath('//img[@alt="imgaa"]').click()
handleAcceptAlert(driver)

# 点击getAllAttributes后获取富文本框内容
driver.find_element_by_xpath('//input[@type="button" and @value="Get All Attributes"]').click()
print('富文本框内容：',driver.find_element_by_id('output').get_attribute('value'))

print('测试完成')
driver.quit()

