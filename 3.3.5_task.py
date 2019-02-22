import sys
import re

_output = [print(line.rstrip()) for line in sys.stdin if re.findall(r"\b(.+)\1\b", line.rstrip())]
