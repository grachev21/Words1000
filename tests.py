from selenium import webdriver
from selenium.webdriver.common.by import By
import time





driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/login/')
driver.find_elements(By.CLASS_NAME, 'login_form_input')[0].send_keys('grachev21')
driver.find_elements(By.CLASS_NAME, 'login_form_input')[1].send_keys('rgir28febk')
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'button_login').click()
time.sleep(1)
driver.find_elements(By.CLASS_NAME, 'dropdown-item')[1].click()


while True:

    with open('clue_index.txt', 'r') as file_object:
        num = file_object.readline()
    with open('clue_en.txt', 'r') as file_object:
        en = file_object.readline()
    with open('clue_ru.txt', 'r') as file_object:
        ru = file_object.readline()
    if driver.current_url != 'http://127.0.0.1:8000/reading_sentences/':
        time.sleep(1)
        learn_new_words = driver.find_elements(By.CLASS_NAME, 'value_words')[int(num)].click()
        time.sleep(1)
        driver.find_elements(By.CLASS_NAME, 'user_form_add_word_accum')[0].send_keys(en)
        driver.find_elements(By.CLASS_NAME, 'user_form_add_word_accum')[1].send_keys(ru)
        time.sleep(1)
        learn_new_words =driver.find_element(By.CLASS_NAME, 'button_result_true').click()
        time.sleep(1)
    else:
        learn_new_words =driver.find_element(By.CLASS_NAME, 'link_next').click()
        time.sleep(1)

driver.quit()

