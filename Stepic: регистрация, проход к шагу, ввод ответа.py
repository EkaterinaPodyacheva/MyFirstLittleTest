import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


try:
    browser = webdriver.Chrome()

    browser.get("https://stepik.org")
    time.sleep(1)
    enter = browser.find_element(By.XPATH, "//a[@id='ember246']")
    enter.click() #Регистрируемся
    time.sleep(1)

    browser.switch_to.window(browser.window_handles[0])
    email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    email.clear()
    email.send_keys("*****")
    time.sleep(1)

    password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    password.clear()
    password.send_keys("*****")
    time.sleep(1)

    password.send_keys(Keys.ENTER) #нажимаем Enter
    #browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  #кликаем
    time.sleep(3)

#ищем курс
    input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Название курса, автор или предмет']")
    input.send_keys("Автоматизация тестирования с помощью Selenium и Python")
    input.send_keys(Keys.ENTER)
    time.sleep(7)

#кликаем на нужный курс
    browser.switch_to.window(browser.window_handles[0])
    course = browser.find_element(By.XPATH, "//a[@aria-label='Автоматизация тестирования с помощью Selenium и Python']")
    course.click()
    time.sleep(5)

#кликаем на нужный раздел модуля и шаг раздела
    #browser.execute_script("window.scrollBy(0, 250);")
    time.sleep(3)
    item2 = browser.find_element(By.XPATH, "//div[@class='toc-syllabus__section'][2]/div[2]/div[3]")    #Динамический id
    item2.click()
    time.sleep(5)
    item2_4 = browser.find_element(By.XPATH, "//div[@data-step-position='4']").click()     #Динамический id
    time.sleep(3)

#вводим ответ в поле
    input_answer = browser.find_element(By.XPATH, "//textarea[@spellcheck='false']").send_keys("123")
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
