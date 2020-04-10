import math
import time
from selenium import webdriver


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_xpath('//*[@id="treasure"]')
    x_element_val = x_element.get_attribute('valuex')
    print(x_element_val)
    y = calc(x_element_val) # присваиваем переменной результат вычисления ф-ии калк

    area_field = browser.find_element_by_xpath('//*[@id="answer"]')
    area_field.send_keys(y)

    cap_check = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    cap_check.click()

    rb_rule_radio = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    rb_rule_radio.click()

    submit_btn = browser.find_element_by_xpath('/html/body/div/form/div/div/button')
    submit_btn.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()