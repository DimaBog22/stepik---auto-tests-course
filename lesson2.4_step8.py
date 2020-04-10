from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

button = browser.find_element(By.ID, 'book')
button.click()

x_number_raw = browser.find_element(By.ID, 'input_value') # инициализируем значение из айди
x_number = int(x_number_raw.text) # выводим его значение и приводим его к числу
result = math.log(abs(12 * math.sin(x_number))) # решаем задачу

answer_input = browser.find_element(By.ID, 'answer')
answer_input.send_keys(str(result)) # вписываем в инпут для ответа ответ, но приведенных при этом к строке

final_submit_btn = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
final_submit_btn.click()