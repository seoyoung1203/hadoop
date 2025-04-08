
# hadoop command
- ls 
    - hdfs dfs -ls / 
    - hdfs dfs -ls<내가 확인하고 싶은 경로> 

- mkdir
    - 생성하고 싶은 폴더 만드는 명령어
    - hdfs dfs -mkdir /input
    - hdfs dfs -mkdir <생성하고 싶은 폴더 이름>

- put
    - hdfs dfs -put <업로드할 파일경로> <업로드할 위치>

- cat
    - hdfs dfs -cat <출력하고싶은 파일 경로> 
    - 출력하고싶은 파일 전체 출력(텍스트로 이루어진 파일만 출력가능)

- head. tail
    - hdfs dfs -heab,tail <출력하고싶은 파일 경로>

- '-rm'
    - hdfs dfs -rm <지울 파일 경로>
    - 폴더를 삭제할 경우 -r 옵션 추가

- | >> 왼쪽의 실행 결과를 오른쪽에 넘겨주세요

------------

# MapReduce

- mapper.py
1) for line in sys.stdin: # 내가 불러오는 파일의 한줄한줄을 line이라는 변수에 저장. (stdin >> 불러오는 파일 전체) ->splitting 과정

2) word, value = line.split('\t') 
   news,  1

- 터미널
    - cat text.txt | python3 mapper.py | sort | python3 reducer.py >> happy1 hello2 news1
                        쪼개고            정렬       갯수 세기



- reducer.py


## 0.wordcount

- 데이터 어디서 , 어디서 저장 ,mapper 어디 ,reducer 어디
```shell
hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -input /input/text.txt -output /output/wordcount -mapper /home/ubuntu/damf2/hadoop/0.wordcount/mapper.py -reduce /home/ubuntu/damf2/hadoop/0.wordcount/reducer.py 
```

- chmod + >> 실행권한 부여

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