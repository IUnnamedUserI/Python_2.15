#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Имя файла не указано. Используйте python"
              " individual_2.py <имя файла>", file=sys.stderr)
        sys.exit(1)
    else:
        with open("individual_2.txt", "r", encoding="utf-8") as file:
            strings = file.readlines()
        
        prev_word = None
        for idx, line in enumerate(strings):
            words = line.strip().split()
            for word in words:
                if (prev_word == word):
                    print(f"В строке {idx + 1} слово '{word}' повторяется дважды")
                prev_word = word
    