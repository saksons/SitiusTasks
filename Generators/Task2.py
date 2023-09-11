"""
Пусть дан текст:

t = "Генератор – это итератор, элементы которого
можно перебирать (итерировать) только один раз.
Итератор – это объект, который поддерживает функцию next()
для перехода к следующему элементу коллекции."

Написать функцию-генератор для выделения слов из этого текста (слова разделяются пробелом, либо переносом строки ‘\n’).
"""

t = """Генератор – это итератор, элементы которого
можно перебирать (итерировать) только один раз.
Итератор – это объект, который поддерживает функцию next()
для перехода к следующему элементу коллекции."""


def boldText(text: str):
    for i in text.split(' '):
        if "\n" in i:
            yield i.upper(), "\n"
            continue
        yield i.upper(), ' '


for word, endpoint in boldText(t):
    print(word, end=endpoint)
