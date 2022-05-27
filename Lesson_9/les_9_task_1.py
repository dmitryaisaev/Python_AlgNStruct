# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.

from hashlib import sha1

def sub_search(s: str, sub: str) -> int:
    len_sub = len(sub)
    h_sub = sha1(sub.encode('utf-8')).hexdigest()
    sub_cnt = 0
    for i in range(len(s) - len_sub + 1):
        if h_sub == sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            return i
    return  -1

str = input('Введите строку ')
str_length = len(str)
sstr_cnt = 0
lst = []

for i in range(0, str_length + 1):
    for j in range(i + 1, str_length + 1):
        if i == j or (i == 0 and j == str_length):
            continue
        sstr = str[i:j]
        if sub_search(str, sstr) != -1:
            lst.append((sstr, sha1(sstr.encode('utf-8')).hexdigest()))

print(lst)
print('Количество подстрок =',  len(lst))