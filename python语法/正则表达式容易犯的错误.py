import re

a = re.sub('[o]', '_', "oooOO", re.IGNORECASE)
print(a)
a = re.sub('[o]', '_', "oooOO", flags=re.IGNORECASE)
print(a)
