import sys
import re

_output = [print(re.sub(r"human", "computer", line.rstrip())) for line in sys.stdin]
