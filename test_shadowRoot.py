from selenium import webdriver
import pytest
from sahitest.conftest import *

# shadow-root标签其实就是一个shadowDOM，它是前端的一种页面封装技术，您可以将shadow DOM视为“DOM中的DOM”（可以看成一个隐藏的DOM）。
# 它是一个独立的DOM树，具有自己的元素和样式，与原始文档DOM完全隔离。
# ShadowDOM 必须附在一个HTML元素中，存放shadowDOM的元素，我们可以把它称为宿主元素。在HTML5中有很多的标签样式都是通过shadowDOM来实现的。


@pytest.mark.usefixtures('connect')
class TestShadowRoot:
    def getText(self, id_name, driver):
        js = 'return document.getElementById("'+id_name+'").innerHTML'
        return driver.execute_script(js)

    @pytest.mark.parametrize('text',['123','456'])
    def test_nameTag(self, connect:webdriver, text):
        driver = connect
        res = self.getText('nameTag',driver)
        print('My name默认值：',res)
        driver.find_element_by_id('newName').clear()
        driver.find_element_by_id('newName').send_keys(text)
        driver.find_element_by_tag_name('button').click()
        js = 'return document.getElementById("nameTag").innerHTML'
        res = driver.execute_script(js)
        assert text == res
        res = self.getText('nameTag',driver)
        print('My name修改后：', res)

    def test_clickTest(self,connect:webdriver):
        driver = connect
        js = 'return document.getElementById("clickTest").innerHTML'
        beforeClick = driver.execute_script(js)
        print('点击前：',beforeClick)
        # 以下方式报错
        # js = 'document.getElementById("shadow-text").click()'
        js = 'document.getElementById("clickTest").shadowRoot.getElementById("shadow-text").click()'
        driver.execute_script(js)
        afterClick = self.getText('clickTest',driver)
        print('点击后：', afterClick)
        assert "click" == afterClick
        # 以下方式报错
        # driver.find_element_by_id('clearResult').click()
        js = 'document.getElementById("clickTest").shadowRoot.getElementById("clearResult").click()'
        driver.execute_script(js)
        afterClear = self.getText('clickTest',driver)
        print('点击clear按钮：', afterClear)

    def test_headingTest(self,connect:webdriver):
        driver = connect
        js = 'return document.getElementById("headingTest").shadowRoot.children'
        shadowRoot = driver.execute_script(js)
        for child in shadowRoot:
           print(child.text)


if __name__ == '__main__':
    pytest.main(['-s','test_shadowRoot.py'])
