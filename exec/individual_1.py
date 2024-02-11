#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == "__main__":
    words = {
        '0': 'Ноль',
        '1': 'Один',
        '2': 'Два',
        '3': 'Три',
        '4': 'Четыре',
        '5': 'Пять',
        '6': 'Шесть',
        '7': 'Семь',
        '8': 'Восемь',
        '9': 'Девять',
        '10': 'Десять'
    }

    with open("individual_1.txt", "r", encoding="utf-8") as file:
        sentences = file.readlines()
        for sentence in sentences:
            for digit, word in words.items():
                sentence = sentence.replace(digit, word)
            print(sentence)
