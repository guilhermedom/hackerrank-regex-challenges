Regex_Pattern = r"^[a-zA-Z24680]{40}[\s13579]{5}$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
