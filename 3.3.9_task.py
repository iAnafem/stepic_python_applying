import sys
import re

_output = [print(re.sub(r"(\w)\1*", r"\1", line.rstrip())) for line in sys.stdin]
