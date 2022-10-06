import re
import json
from regex.expr import RegexAdapter

regA = RegexAdapter()

src = "test/eng/test0.py"

f = open(src, "r")
script = f.read()

print(script)
print(regA.replace_all_keywords(script))
