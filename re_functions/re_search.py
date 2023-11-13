import re

# Напишите программу, которая найдёт первый хештег в тексте и выведет его в консоль.

print(result[0] if (result := re.search(r'#[a-z]+', input())) else 'There are no hashtags :(')


# У Илона Маска на компьютере хранится очень много важных данных. Для запуска ракеты
# на Марс нужен секретный код, который был утерян. Илон написал программу, которая
# открывает все файлы на компьютере по очереди и проходит по каждой его строке
# (4 строки за один проход). Допишите его программу так, чтобы она находила слово
# "Код" или "код". У Илона больше нет никаких секретных кодов на компьютере,
# поэтому он решил использовать re.search(), т.к. re.search() находит только
# первое вхождение в строке.
#
# Илон не помнит из каких символов он составлен, а также его длину, но он точно
# помнит, что перед самим кодом было написано слово код или Код. Если помочь Илону
# и сказать на какой строке и в каком её месте есть слово код, то он сразу
# сможет его найти.
#
# Если в этих строках кода нет - нужно вывести строку: код не найден.

for num in range(1, 5):
    match = re.search(r"[Кк]од", input())
    if match:
        print(num, match.start())
        break
else:
    print("код не найден")


# Вы получили доступ к секретному чату, в котором часто дарят ключи от Windows 7,
# и решили украсть один из них, т.к. у вас не активирован Windows 7. Вы выкачали
# все сообщения от новых к старым и проходите по ним программой.

#  Нужно найти первый попавшийся ключ. Нужные ключи в чате всегда отправляют в виде:
#
# Activation key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
# X - любая цифра или латинская буква в верхнем регистре
# Перед нужным ключом должна стоять строка Activation key:

g = r"[\dA-Z]{5}"

for _ in range(5):
    match = re.search(rf"(?<=Activation key: ){g}-{g}-{g}-{g}-{g}", input())
    if match:
        print(match.group())
        break


# Даны данные в формате JSON. С помощью регулярных выражений нужно получить
# ключ t и его значение.

# Нужно найти ключ t и его значение:
#
# Значением является последовательностью из арабских цифр, символов . и +
# Перед значением стоит t=

match = re.search(r't=[0-9.+]+', input())
print(match.group())
