import sys
import re

pattern = r"(\b(\w+)\2\b)"

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) != None:
        print(line)