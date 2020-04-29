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

distances = {
    (x1, y1) = Moscow
    (x2, y2) = London
    "Moscow-London": ((x1 - x2) ** 2 + (y1 - y2) ** 2) * 0.5
}

# TODO здесь заполнение словаря

print(distances)




