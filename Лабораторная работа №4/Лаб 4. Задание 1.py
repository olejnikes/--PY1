def get_count_char(str_):
    dictionary_ = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for words in str_:
        if words.isalpha():
            if words in dictionary_:
                dictionary_[words] += 1
            else:
                dictionary_[words] = 1
    return dictionary_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
