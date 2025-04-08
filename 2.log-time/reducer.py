
import sys

last_hour = None
total_count = 0

# 03    1
# 03    1
# 04    1
# 05    1

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
