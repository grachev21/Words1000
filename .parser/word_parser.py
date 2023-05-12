#!/usr/bin/python
# -*- coding: utf-8 -*- import record_csv import re from time import sleep

import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import record_csv


class ReadWordList:
    asdfasdf = 'dfdf'

    def __init__(self):
        '''Инцилизация переменных'''
        self.file = 'words'
        self.list_words = []

    def read(self):
        '''Вычитывает слова на английском'''

        with open(self.file, 'r') as File:
            line = File.readlines()
        return line


class Translate:

    def __init__(self, list_words):
        self.words_list = list_words
        self.user = 'Mozilla/5.0 (X11; Linux x86_64) AppleWeb"\
                "Kit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        self.option = webdriver.FirefoxOptions()

    def config(self):
        self.option.set_preference("dom.webdriver.enabled", False)
        self.option.set_preference("dom.webnotifications.enabled", False)
        self.option.set_preference('general.useragent.override', self.user)
        self.option.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.option)

        self.driver.get('https://wooordhunt.ru/')


    def translate(self):
        '''Переводит слова'''

        def parsing_html(html, word):
            '''Парсит html'''

            exemple_en = ''
            exemple_ru = ''

            bs = BeautifulSoup(html, 'html.parser')
            block = bs.find('div', {'id':'content_in_russian'})
            title = bs.find('div', {'id':'wd_title'})

            # Слово
            word = word
            # Транскрипция
            transcription = title.find('span', {'class':'transcription'})
            # Перевод
            translation = block.find('div', {'class':'t_inline_en'})
            # Фразы
            for bk in block.find_all('p', {'class':re.compile('ex_o|ex_t')}):
                if 'ex_o' in str(bk):
                    exemple_en += f'-->>> {bk.get_text().strip()}'
                if 'ex_t' in str(bk):
                    exemple_ru += f'-->>> {bk.get_text().strip()}'
            return [word,
                    transcription,
                    translation,
                    exemple_en,
                    exemple_ru]

        input_id = "//input[@id='hunted_word']"
        input_id_submit = "//input[@id='hunted_word_submit']"
        count = 1

        # Перебор слов на сайте
        for word in self.words_list:
            print(count)
            count += 1

            search = self.driver.find_element(By.XPATH, input_id).clear()
            search = self.driver.find_element(By.XPATH, input_id)\
                    .send_keys(word)
            sleep(0.5)
            run = self.driver.find_element(By.XPATH, input_id_submit ).click()
            sleep(0.5)

            # html получаем бок всей страницы
            html = self.driver.page_source

            # Передаем блок html в функцию для разбора абзаццов.
            data_table = parsing_html(html, word=word)

            # Запись в csv
            record_csv.record(data_table)

        self.driver.quit()

def main():

    word_parser = ReadWordList()
    list_words = word_parser.read()

    site_parser = Translate(list_words)
    site_parser.config()
    site_parser.translate()

    # words.parsing_words()


if __name__ == '__main__':
    main()


