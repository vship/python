#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}
distances['Moscow'] = {}
(x1, y1) = sites['Moscow']
(x2, y2) = sites['London']
distances['Moscow']['London'] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) * 0.5
(x1, y1) = sites['Moscow']
(x2, y2) = sites['Paris']
distances['Moscow']['Paris'] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) * 0.5
distances['London'] = {}
(x1, y1) = sites['London']
(x2, y2) = sites['Paris']
distances['London']['Paris'] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) * 0.5
(x1, y1) = sites['Moscow']
(x2, y2) = sites['London']
distances['London']['Moscow'] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) * 0.5
distances['Paris'] = {}
(x1, y1) = sites['Moscow']
(x2, y2) = sites['Paris']
distances['Paris']['Moscow'] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) * 0.5
(x1, y1) = sites['London']
(x2, y2) = sites['Paris']
distances['Paris']['London'] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) * 0.5

# TODO FINISH

print(distances)
city1 = input('введите город: ')
city2 = input('Введите город 2: ')

print('Расстояние от ' + city1 + ' до ' + city2 + ' ' + str(distances[city1][city2]) + ' КМ')



