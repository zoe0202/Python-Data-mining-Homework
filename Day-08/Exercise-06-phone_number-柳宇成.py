import re

text = input('请输入提取文本：')
result = re.findall(r'13\d{9}|14\d{9}|15\d{9}|16\d{9}|17\d{9}|18\d{9}|19\d{9} ', text)
print(result)

