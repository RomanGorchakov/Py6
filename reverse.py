#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import string
import random


if __name__ == '__main__':
    dictionary = {}
    length = random.randint(4, 12)
    key = 0

    for elem in range(0, length):
        s = random.randint(6, 15)
        stroka = "".join(random.choices(string.ascii_letters + string.digits, k = s))
        dictionary[key] = stroka
        key += 1
    print(dictionary)
    
    items = dictionary.items()
    rev = dict(reversed(items) for items in dictionary.items())
    print(rev)