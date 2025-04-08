#!/usr/bin/env python3 >> 

import sys

# line이라는 변수에 저장. (stdin >> happy 1, news 1)

last_word = None
total_count = 0

for line in sys.stdin:
    word, value = line.split('\t') # word -> 단어, value ->1
    value = int(value)

    if last_word == word:
        total_count += value # 같은 단어면 value(1) 값 추가할거얌
    else:
        if last_word is not None: # 연속되는 상황, 계속되서 출력
            print(f'{last_word}\t{total_count}')
        last_word = word #(last_word를 현재 word로)
        total_count = value # (초기화)

if last_word == word:
    print(f'{last_word}\t{total_count}')

    # cat text.txt | python3 mapper.py | sort | python3 reducer.py >> happy1 hello2 news1
#                           쪼개고       정렬       갯수 세기