import re
a="126_ani0918653305155_%^qj718564"
def judge_phone_number(a):
    b=re.findall("(18\d[^123]3{2}0+[3|5]\d5{2})", a)

    return b
print("电话为：",judge_phone_number(a))