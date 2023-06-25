from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

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
driver.get("http://127.0.0.1:8000/learn_new_words/")


for number in range(0, 1000000):
    value = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[4]/div/a").click()
    print(number)
