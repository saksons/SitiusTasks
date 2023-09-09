"""
Разработайте программу, которая будет показывать слово (или слова),
чаще остальных встречающееся в текстовом файле(файл для проверки можно ручками создать). Сначала пользователь
должен ввести имя файла для обработки. После этого вы должны открыть
файл и  проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры
"""

prep = [',', '.', '/', '\'', ';', ':', '"', '!', '@', '#', '№', '$', '%', '^', '&', '*', '(', ')', '~', '\n', '\t', '?']
words_ = dict()


def getFormedLine(file: str):
    with open(file, 'r', encoding="utf-8") as file:
        for line in file:
            for _ in prep:
                line = line.replace(_, '')
            yield line.split(' ')


def getWordByDict(words: dict, word: str):
    if word in list(words.keys()):
        return True
    return False


def countWords(words: dict):
    for lineOfWords in getFormedLine("test.txt"):
        for word in lineOfWords:
            if getWordByDict(words=words, word=word):
                words_[word] = int(words_[word]) + 1
            else:
                words_[word] = 1
    return words_

def main():
    dictOfWords = countWords(words_)
    maxValue = list(dictOfWords.values())[0]
    word = list(dictOfWords.keys())[0]
    for k,v in dictOfWords.items():
        if v > maxValue:
            maxValue = v
            word = k
    return word


if __name__ == "__main__":
   print( main())