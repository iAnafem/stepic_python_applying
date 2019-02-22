import sys
import re

_output = [print(re.sub(r"\b[Aa]+\b", "argh", line.rstrip(), count=1)) for line in sys.stdin]
