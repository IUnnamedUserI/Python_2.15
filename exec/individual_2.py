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
        words_seen = {}
        for idx, line in enumerate(strings):
            words = line.strip().split()
            for word in words:
                if (prev_word == word):
                    print(f"В строке {idx} слово '{word}' повторяется дважды")
                elif word in words_seen:
                    if idx != words_seen[word]:
                        print(f"В строке {idx} слово '{word}' повторяется"
                                " на строке {words_seen[word]}")
                prev_word = word
    