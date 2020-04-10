import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_value_raw = browser.find_element(By.ID, 'input_value')
    x_value = x_value_raw.text
    print(x_value)

    result = math.log(abs(12* math.sin(int(x_value))))
    print(result)

    browser.execute_script("window.scrollBy(0, 150);")

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(str(result))

    isnt_robot_btn = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/label')
    isnt_robot_btn.click()

    robots_rule_radio = browser.find_element(By.XPATH, '/html/body/div/form/div[4]/label')
    robots_rule_radio.click()

    submit_btn = browser.find_element(By.TAG_NAME, 'button')
    submit_btn.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()