import csv
import os
from bs4 import BeautifulSoup

header = ('Английский',
          'Транскрипция',
          'Русский',
          'Фраз.en',
          'Фраз.ru')

def record(table):
    '''Как так'''

    if table[1] != None:
        table[1] = table[1].get_text()
    if table[2] != None:
        table[2] = table[2].get_text()


    check_file = os.path.isfile('db_1000_words.csv')
    csvFile = open('db_1000_words.csv', 'a')

    try:

        writer = csv.writer(csvFile)

        # Если такой файл не существует создаем шапку
        if check_file:
            writer.writerow(table)
        else:
            writer.writerow(header)
            writer.writerow(table)

    finally:
        csvFile.close()
