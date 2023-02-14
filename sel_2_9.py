from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


try:

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем Submit
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Считываем x
    x = browser.find_element(By.ID, "input_value").text

    # Считаем математическую функцию
    y = calc(x)

    # Вводим ответ в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(y)

    # Нажимаем Submit
    browser.find_element(By.XPATH, "//button[@type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()