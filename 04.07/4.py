import string

text = input("Введите текст: ").lower()

for i in text:
  if i in string.punctuation:
    text = text.replace(i, "")

list = text.split()
dc = {}

for i in list:
  dc.setdefault(i, 0)
  dc[i] += 1

for i in sorted(dc.items()):
    if i[1] == min(dc.values()):
        print(f"Реже всего встречается: {i[0]}")
        break


# Введите текст: один. Два, два? ОДин. два
# Реже всего встречается: один        
        
# Введите текст: Для современного мира граница обучения кадров прекрасно подходит для реализации соответствующих условий активизации.
# Реже всего встречается: активизации

# Введите текст: Имеется спорная точка зрения, гласящая примерно следующее: явные признаки победы институционализации представляют собой не что иное, как квинтэссенцию победы маркетинга над разумом и должны быть разоблачены.
# Реже всего встречается: быть

