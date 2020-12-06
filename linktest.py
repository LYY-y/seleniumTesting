from selenium import webdriver

driver = webdriver.Chrome("F:\chromedriver_win32\chromedriver.exe")
driver.get("http://sahitest.com/demo/linkTest.htm")

# 通过内容识别链接
print(driver.find_element_by_link_text("linkByContent").text)

# 通过id识别
print(driver.find_element_by_id("linkByHtml").text)

# 通过部分内容识别
print(driver.find_element_by_link_text("link without href").text)

# 点击链接返回true，顺利跳转到另一个页面
driver.find_element_by_link_text("link with return true").click()
# 另一个页面有弹出提示框
alert = driver.switch_to.alert
alert.accept()
driver.back()
print(driver.find_element_by_id("t1").get_attribute("value"))

# 点击链接返回false，无法跳转到另一个页面
driver.find_element_by_xpath("/html/body/a[5]").click()
print(driver.find_element_by_id("t1").get_attribute("value"))

# 点击链接返回值为false，无法跳转到另一个页面
driver.find_element_by_link_text("link with returnValue=false").click()
print(driver.find_element_by_id("t1").get_attribute("value"))

# 点击链接触发js
driver.find_element_by_link_text("added handler using js").click()
print(driver.find_element_by_id("t1").get_attribute("value"))

# 图片上带链接
driver.find_element_by_css_selector("body > a:nth-child(25) > img").click()
driver.back()
driver.find_element_by_id("imageLink2")
print(driver.find_element_by_id("t1").get_attribute("value"))

# 点击链接弹出对话框
driver.find_element_by_css_selector("body > a:nth-child(35) > span").click()
# 获取alert对话框内容
alert = driver.switch_to.alert
print("对话框内容：",alert.text)
alert.accept()

# 点击正常数字的链接
driver.find_element_by_link_text("1234").click()
driver.back()

# 点击<em>标签下的链接
driver.find_element_by_link_text("Sahi").click()
driver.back()

# 点击链接为#，但在js中跳转的链接
driver.find_element_by_link_text("Form submit on click").click()
# 另一个页面有弹出提示框
alert = driver.switch_to.alert
alert.accept()
driver.back()


# 使用title属性定位链接
print(driver.find_element_by_xpath("//a[@title='with title']").text)


# 图片链接返回false，不跳转
driver.find_element_by_id("imageWithReturnFalse").click()

# 点击后触发js，使该节点的父节点的href为tableTest.htm
driver.find_element_by_id("imageWithOnclickChangingHref").click()
driver.back()

# 切入到iframe
driver.switch_to.frame('myframe')
driver.find_elements_by_tag_name('div')[0].click()
print(driver.find_element_by_id('tb').get_attribute('value'))

# 切回主页面
driver.switch_to.default_content()

# 点击改变iframe的链接
print("当前iframe的url", driver.find_element_by_id('myframe').get_attribute('src'))
driver.find_element_by_link_text('click here').click()
driver.switch_to.frame('myframe')
driver.switch_to.default_content()
print("退出iframe的url", driver.find_element_by_id('myframe').get_attribute('src'))

# 返回index页面
driver.find_element_by_link_text('Back').click()
print(driver.current_url)

driver.quit()