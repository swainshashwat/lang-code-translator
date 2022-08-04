import re
import json
from regex.expr import regex_keywords

src = "test/eng/test0.py"

f = open(src, "r")
script = f.read()

print(script)
print(regex_keywords)
