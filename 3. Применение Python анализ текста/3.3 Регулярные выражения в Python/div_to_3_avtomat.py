import sys
import re


pattern = r"^(0|(1(0(1)*0)*1))+$"

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern,line):
        print(line)