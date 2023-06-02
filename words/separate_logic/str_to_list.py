def str_list(value_en, value_ru):
    value_list_en = []
    value_list_ru = []
    base_list = []
    value_en = value_en.split('-->>> ')
    value_ru = value_ru.split('-->>> ')


    for vn in value_en:
        if vn != '':
            value_list_en.append(vn)


    for vu in value_ru:
        if vu != '':
            value_list_ru.append(vu)

    count = 0

    for v in value_list_ru:
        base_list.append(value_en[count])
        base_list.append(value_ru[count])
        count += 1

        # del base_list[0]
    return base_list






