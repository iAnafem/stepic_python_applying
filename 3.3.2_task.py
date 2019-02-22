import sys
import re

_output = [print(line.rstrip()) for line in sys.stdin if re.findall(r"\bcat\b", line.rstrip())]
