
# hadoop command

- hive서버 실행 -> hadoop 필요
- cd hadoop-3.3.6/ >> 하둡 폴더로 이동
- ubuntu@1-16:~/hadoop-3.3.6$ : sbin/start-all.sh >> 하둡 실행(백그라운드에서 실행) -> 하둡 종료: sbin/stop-all.sh

- cd ../hive -로 이동(matadata store 생성을 실행하면 내가 있는 위치에 matastore db 생성)

- hiveserver2 --hiveconf hive.server2.thrift.port=10000 --hiveconf hive.root.logger=DEBUG,console(hive 서버 실행 (metastore_db 있는 폴더에서)) >> 테이블 구조 저장 가능
-------

- input > book > books, ratings,users (파일)
-------

- ls 
    - hdfs dfs -ls / 
    - hdfs dfs -ls<내가 확인하고 싶은 경로> 

- mkdir [폴더 만들고]
    - 생성하고 싶은 폴더 만드는 명령어
    - hdfs dfs -mkdir /input
    - hdfs dfs -mkdir <생성하고 싶은 폴더 이름>

- put[데이터 업로드]
    - hdfs dfs -put <업로드할 파일경로> <업로드할 위치(hdfs의 경로)> 파일 구조 다 적기(어느 위치에 있는지)
                                    하둡 경로라 자동완성 x

- cat
    - hdfs dfs -cat <출력하고싶은 파일 경로> 
    - 출력하고싶은 파일 전체 출력(텍스트로 이루어진 파일만 출력가능)

- head. tail
    - hdfs dfs -heab,tail <출력하고싶은 파일 경로>

- '-rm'
    - hdfs dfs -rm <지울 파일 경로>
    - 폴더를 삭제할 경우 -r 옵션 추가

- | >> 왼쪽의 실행 결과를 오른쪽에 넘겨주세요

- wget <다운로드 주소>

- bashrc. 수정하면 >> source ~/.bashrc(새로고침) 필수 (터미널 껐다가 켜도 됨)
--------

# MapReduce

## 0.wordcount

- 데이터 어디서 , 어디서 저장 ,mapper 어디 ,reducer 어디
```shell
hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -input /input/text.txt -output /output/wordcount -mapper /home/ubuntu/damf2/hadoop/0.wordcount/mapper.py -reduce /home/ubuntu/damf2/hadoop/0.wordcount/reducer.py 
```

- chmod + >> 실행권한 부여

- mapper.py

1) for line in sys.stdin: # 내가 불러오는 파일의 한줄한줄을 line이라는 변수에 저장. (stdin >> 불러오는 파일 전체) ->splitting

2) line = line.strip() #좌우 띄어쓰기 없애기

3) words = line.split() # 줄별로 쪼개고

4) for word in words: # 단어로 쪼개

5) print(f'{word}\t1') # 간격을 두세요

- reducer.py

1) for line in sys.stdin: # 내가 불러오는 파일의 한줄한줄을 line이라는 변수에 저장. (stdin >> 불러오는 파일 전체) ->splitting 과정

2) word, value = line.split('\t') 
   news,  1

3)  if last_word == word:
        total_count += value # 같은 단어면 value(1) 값 추가할거얌

4) else:
        if last_word is not None: # 연속되는 상황, 계속되서 출력

5) last_word = word #(last_word를 현재 word로)
   total_count = value # (초기화)

- 터미널
    - cat text.txt | python3 mapper.py | sort | python3 reducer.py >> happy1 hello2 news1
                        쪼개고            정렬       갯수 세기


---------

## 1. movie-rate-avg


```shell
import sys

currunt_movie_id = None
currunt_sum = 0
currunt_count = 0

for line in sys.stdin:
    movie_id, rating = line.split('\t')

    try:
        rating = float(rating)
    except:
        continue

    if currunt_movie_id == movie_id:
        currunt_count += 1
        currunt_sum += rating
    else: # 영화가 바뀐 지점
        if currunt_movie_id is not None:
            currunt_avg = currunt_sum / currunt_count
            print(f'{currunt_movie_id}\t{currunt_avg}')

        currunt_movie_id movie_id
        currunt_count = 1
        currunt_sum = rating

currunt_avg = currunt_sum / currunt_count
print(f'{currunt_movie_id}\t{currunt_avg}')
```

```shell
import sys
last_hour = None
total_count = 0

for line in sys.stdin:
    line = line.strip()

    hour, value = line.split()
    value = int(value)

    if last_hour == hour:
        total_count += value
    else:
        if last_hour is not None:
            print(f'{last_hour}\t{total_count}')

        last_hour = hour
        total_count = value
print(f'{last_hour}\t{total_count}')
```



