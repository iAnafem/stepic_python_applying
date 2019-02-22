import sys
import re

_output = [print(re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line.rstrip())) for line in sys.stdin]


