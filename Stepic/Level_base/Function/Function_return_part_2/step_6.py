# объявление функции
def is_one_away(word1, word2):
    flag = False
    if len(word1) == len(word2):
        total = 0
        for i in range (len(word1)):
            if word1[i] != word2[i]:
                total+=1
        if total == 1:
            flag = True
    return flag 

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))