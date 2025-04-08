import sys

for line in sys.stdin:
    line = line.strip()

    fields = line.split(',')
    # ['1', '296', '5.0', '11133451414']

    movie_id = fields[1]
    rating = fields[2]

    print(f'{movie_id}\t{rating}')