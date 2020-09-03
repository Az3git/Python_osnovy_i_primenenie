import sys
import re

pattern = r"(cat).{0,}\1"

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) != None:
        print(line)

