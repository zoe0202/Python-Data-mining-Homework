import re
source = '1234"https://abc.def.com/9012"5678'
source1 = re.split('"',source)
pattern = r'https://+[a-zA-Z0-9-/.]+'
for i in source1:
    if re.match(pattern,i) is not None:
        print(i)
