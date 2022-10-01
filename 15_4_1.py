# text = []
def changeText(text):
    for i in '.!"\'#$%^&*()-+=,/:;<>?@[\\]_{|}~–':
        text = text.replace(i, '')
        text = text.lower()
    return text.split()

def mostCommon(text):
    count = {}

    for word in text:
        if word in count and len(word) > 3:
            count[word] +=1
        else:
            count[word] = 1
    cnt_max = 0
    word_max = ''
    for word, cnt in count.items():
        if cnt > cnt_max:
            cnt_max = cnt
            word_max = word
    return word_max

def mostLenght(text):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    english_word = []
    for word in text:
        for char in word:
            if char in alpha and word not in english_word:
                english_word.append(word)
            break
    max_word = ''
    for word in english_word:
        if len(word) > len(max_word):
            max_word = word
    return max_word

nameFile = input('Название файла: ')

with open(nameFile, encoding='utf8') as myFile:
    fileText = myFile.read()

fileText = changeText(fileText)

print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText)}')
print(f'Список самых длинных английских слов: {mostLenght(fileText)}')