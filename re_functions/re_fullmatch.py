import re

# Дарья ждёт милого мальчика, который напишет ей ночью: номер, срок действия,
# владельца, CVV. Помогите ей проверить номер банковской карты.

print(True if re.fullmatch(r"\d{13,}", input()) else False)


# Проверьте пароль на валидность

# Проверить пароль на валидность. Валидным будем считать пароль, который:
#
# Состоит из a-z, A-Z, 0-9, @#$%^&*()_-+!?
# Его длина минимум 8 символов

print(bool(re.fullmatch(r'[a-zA-Z0-9@#$%^&*()_+!?-]{8,}', input())))


# Очень часто номера телефонов вводят по-разному. Иногда ставят скобки, иногда
# тире, иногда пробелы, иногда вообще ничего не ставят. Напишите регулярное
# выражение, которое найдёт все такие номера.

# Найдите все последовательности, которые могут быть номерами телефонов:
#
# Номер может начинаться с +
# Потом идут цифры
# В каждом номере минимум 11 цифр
# Между цифрами могут быть разделители: ( )-
# Длина разделителя от 0 до 2 символов включительно



print(re.fullmatch(r'\+?(?:([() -]{0,2})\d([() -]{0,2})){11}', input()))