#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO Final
zoo.insert(zoo.index('lion'), 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO Final
zoo.extend(birds)
print(zoo)
# уберите слона
#  и выведите список на консоль
# TODO Final
zoo.remove('elephant')
print(zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO Final

print('Лев сидит в клетке №' + str(zoo.index('lion') + 1) + ' ,а жаворонок сидит в клетке №' + str(zoo.index('lark') + 1))
