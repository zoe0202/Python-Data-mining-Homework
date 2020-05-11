import re
with open("telephone number.txt","rb") as f:
    text_num = str(f.read())
pattern = re.compile("/d{11}")
tele_num = pattern.finditer(text_num)
for i in tele_num:
    print(i.group())
#不知为什么上面的代码运行出来没有结果，希望师哥师姐可以解答一下
# import re
# text = "356747435435647658754746452"
# num = re.compile(r'\d{11}')
# tele_num = num.match(text)
# print(tele_num)
