class StrList:
    def __init__(self, en, ru):
        self.value_en = en
        self.value_ru = ru
        self.base = []
        self.base_list = []


    def search_long_list(self):
        if len(self.value_en) < len(self.value_ru):
            return self.value_en
        if len(self.value_en) > len(self.value_ru):
            return self.value_ru
        if len(self.value_en) == len(self.value_ru):
            return self.value_en

    def create_dict(self, number):

        for value in range(len(number)):
            # Детект словаря
            self.base.append(dict({'en': self.value_en[value], 'ru': self.value_ru[value]}))


    def create_dict_list_10(self):
        count = 0
        for base_loop in self.base:
            # count ограничивает длинну списка
            if count != 10 and base_loop['en'] != '':
                self.base_list.append(base_loop)
                count += 1

        return self.base_list


def str_list(en, ru):
    print(len(en), len(ru), '<<<<')
    strlist = StrList(en, ru)
    value = strlist.search_long_list()
    strlist.create_dict(value)
    base_list = strlist.create_dict_list_10()
    return base_list