from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click() # нажимаем на кнопку

    confirm = browser.switch_to.alert # переключаемся на конфирм
    confirm.accept() # нажимаем ок

    x_number_raw = browser.find_element(By.ID, 'input_value') # инициализируем значение из айди
    x_number = int(x_number_raw.text) # выводим его значение и приводим его к числу
    result = math.log(abs(12 * math.sin(x_number))) # решаем задачу

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(str(result)) # вписываем в инпут для ответа ответ, но приведенных при этом к строке

    final_submit_btn = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    final_submit_btn.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()