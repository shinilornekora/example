#  Дана строка. Посчитать количество каждого символа в ней.
#  O(N^2) -> O(N)
#  aaccbbbbd -> d 1 \n b 4 \n a 2 \n c 2
#  GitHub -> https://github.com/
#  GitHub - open площадка
#  coding -> commit -> push

def count(s, char):
    counter = 0
    for i in range(len(s)):
        if s[i] == char:
            counter += 1
    return counter

#  Пусть в s у нас n символов. Тогда цикл for, заданный по всей длине строки
#  даст нам N операций. Из-за функции count мы получаем N операций на каждую
#  операцию цикла for. Текущая сложность - O(N**2).


# def symbolCounter(s: str):
#     for i in range(len(s)):
#         print(s.count(s[i]), s[i])


# O(N * M), где N - длина всей строки, M - число уникальных символов в строке

# def symbolCounter(s: str):
#     for sym in set(s):
#         counter = 0
#         for i in s:
#             if sym == i:
#                 counter += 1
#         print(sym, counter)

# O(N) - ?
# Python dictionary - словари.
# Если у нас встречается буква до того не встречавшаяся - {a: 1}
# Если у нас эта буква есть в словаре - {a: n += 1}
# .get(index, accumulator)

# leetcode, codewars - Если хотите потренироваться алгосам
def symbolCounter(s: str):
    syms_counter = {}
    for i in s:
        syms_counter[i] = syms_counter.get(i, 0) + 1
    return syms_counter


print(symbolCounter(input()))


#  Sberbank / Yandex / Tinkoff / Ozon / Alpha
#  1 собес / <2 алгособеса> / команда

# Перерыв до 16:10! Потом будем заниматься настройкой GIT.






