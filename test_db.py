from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

user = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
# Настройка Firefox.
option = webdriver.FirefoxOptions()
# Обход детекты Selenium.
option.set_preference("dom.webdriver.enabled", False)
# Отключаем увидомление.
option.set_preference("dom.webnotifications.enabled", False)
# Передаем user-agent.
option.set_preference('general.useragent.override', user)
# Отключает морду браузера.
# option.add_argument("--headless")

# Передаем настройки драйверу.
driver = webdriver.Firefox(options=option)
driver.set_window_size(1800, 1600)
# Функция ожидания.
driver.implicitly_wait(100)
# Запуск страницы.
driver.get("http://127.0.0.1:8000/login/")

driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys('grachev21')
driver.find_element(By.XPATH, "//*[@id='id_password']" ).send_keys('rgir28febk')
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/button").click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/a[3]").click()

while True:
    with open('clue_index.txt', 'r') as file_object:
        num = file_object.readline()
    with open('clue_en.txt', 'r') as file_object:
        en = file_object.readline()
    with open('clue_ru.txt', 'r') as file_object:
        ru = file_object.readline()

        num = int(num) + 1
    if driver.current_url != 'http://127.0.0.1:8000/reading_sentences/':
        sleep(2)
        print(num, '<<<')
        learn_new_words = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div[3]/form/div/input[{num}]").click()
        print('run_button')
        sleep(2)
        driver.find_element(By.XPATH, "//*[@id='id_word_en']").send_keys(en)
        driver.find_element(By.XPATH, "//*[@id='id_word_ru']").send_keys(ru)
        sleep(2)
        learn_new_words =driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/form/button").click()
        sleep(2)
    else:
        learn_new_words =driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/nav/ol/li/a").click()
        sleep(2)
