import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestAbs(unittest.TestCase):

    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        last_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        email = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')

        first_name.send_keys('Зубенко Михаил Петрович')
        last_name.send_keys('Зубенко Михаил Петрович')
        email.send_keys('Зубенко Михаил Петрович')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        result = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, result)


    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        last_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        email = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')

        first_name.send_keys('Зубенко Михаил Петрович')
        last_name.send_keys('Зубенко Михаил Петрович')
        email.send_keys('Зубенко Михаил Петрович')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        result = "Congratulations! You have successfully registered!"
        self.assertEqual(result, welcome_text)


if __name__ == '__main__':
    unittest.main()

