#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random


if __name__ == '__main__':
    school = {}
    length = int(input("Количество классов: "))

    for elem in range(0, length):
        school[input()] = random.randint(15, 30)
    print(school)

    change = input("Название класса, в котором изменилось количество учеников: ")
    school[change] = random.randint(15, 30)
    print(school[change])
 
    new = input("Название класса, который появился в школе: ")
    school[new] = random.randint(15, 30)
    print(school[new])
 
    del school[input("Название класса, который был расформирован: ")]
 
    print(f"Всего учеников в школе: {sum(school.values())}")