import re

s = re.compile("\\d*\*\\d*\*\\d*.*")
a = "60*08*3*asdeasdo123"
print(s.match(a))
