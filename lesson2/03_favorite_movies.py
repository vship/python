#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код FINAL

print("Первый фильм: " + my_favorite_movies[:my_favorite_movies.find(",")])
print("Последний фильм: " + my_favorite_movies[my_favorite_movies.rfind(",") + 1:])
print("Второй фильм: " + my_favorite_movies[my_favorite_movies.find(",") + 1:my_favorite_movies.find(",", my_favorite_movies.find(",") + 1)])
print("Второй с конца фильм: " + my_favorite_movies[my_favorite_movies.rfind(",", 0, my_favorite_movies.rfind(",")) + 1:my_favorite_movies.rfind(",")])
