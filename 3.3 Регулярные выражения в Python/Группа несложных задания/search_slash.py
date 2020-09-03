import sys
import re

pattern = r"[\\]"

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) != None:
        print(line)