from pprint import pprint


# Чтение из файла данный. Возвращает список текстов новостей
def load_file():
    import xml.etree.cElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse("files/newsafr.xml", parser)
    root = tree.getroot()
    news_data = [
        x.text
        for x in root.findall('channel/item/description')
    ]
    return news_data


# Возвращает список топ 10 самых встречаемых слов длиннее 6 символов
# в формате: [слово, сколько раз встретилось слово].
def top_words(news_data: list):

    # Возвращает список слов (с повторениями) из переданой строки без знаков препинания
    def split_line(line: str):
        import string
        words_list = line.split()
        for index, value in enumerate(words_list):
            words_list[index] = value.strip(string.punctuation)
        return words_list

    words = dict()
    for item in news_data:
        words_in_line = split_line(item)
        for word_item in words_in_line:
            if word_item in words:
                words[word_item] += 1
            else:
                if len(word_item) > 6:
                    words.update({word_item: 1})
    return sorted(words.items(), key=lambda x: x[1], reverse=True)[:10]


def main():
    top = top_words(load_file())
    print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для .json файла')
    for number, word in enumerate(top, 1):
        print(f'{number} - {word[0]} ({word[1]})')


main()
