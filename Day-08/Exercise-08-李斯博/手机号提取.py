import re
text=input('请输入包含电话号码的文本')
output=re.findall(r'13\d{9}|14\d{9}|15\d{9}|16\d{9}|17\d{9}|18\d{9}|19\d{9} ', text)
print(output)
                   