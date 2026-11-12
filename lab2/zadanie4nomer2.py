"""Найти все уникальные слова в тексте, введённом пользователем"""

line = str(input())
slova = set(line.split())
print(slova)