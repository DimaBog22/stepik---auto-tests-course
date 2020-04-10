from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
    last = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
    email = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')

    first.send_keys('ZUBENKO')
    last.send_keys('MIKHAIL')
    email.send_keys('PITROVICH!')

    current_dir = os.path.abspath(os.path.dirname(__file__)) # узнаем нашу директорию
    file_path = os.path.join(current_dir, '1.txt') # инициализируем нужный файл
    upload_element = browser.find_element(By.XPATH, '//*[@id="file"]') # инициализируем кнопку

    upload_element.send_keys(file_path)

    submit_btn = browser.find_element(By.XPATH, '/html/body/div/form/button')
    submit_btn.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()