#!/usr/bin/env python3

import sys

for line in sys.stdin: # 내가 불러오는 파일의 한줄한줄을 line이라는 변수에 저장. (stdin >> 불러오는 파일 전체) ->splitting
    line = line.strip() #좌우 띄어쓰기 없애기
    words = line.split() # 줄별로 쪼개고
    # ['happy', 'today']

    for word in words: # 단어로 쪼개
        print(f'{word}\t1') # 간격을 두세요