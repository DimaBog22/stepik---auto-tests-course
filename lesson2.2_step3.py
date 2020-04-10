import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_number_raw = browser.find_element(By.ID, 'num1')
    second_number_raw = browser.find_element(By.ID, 'num2')

    first_number = int(first_number_raw.text)
    second_number = int(second_number_raw.text) # приводим к числу для арифметических операций

    sum_numb = first_number + second_number
    print(sum_numb)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(sum_numb)) # приводим к строке для вывода

    btn = browser.find_element(By.XPATH, '/html/body/div/form/button')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()