import sys
import re

_output = [print(line.rstrip()) for line in sys.stdin if len(re.findall("cat", line.rstrip())) >= 2]



