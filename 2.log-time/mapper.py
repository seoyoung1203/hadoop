
import sys
import re

time_pattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})')

for line in sys.stdin:
    line = line.strip()

    match = time_pattern.search(line)
  
    
    if match:
        hour = match.group(1)
        print(f'{hour}\t1')