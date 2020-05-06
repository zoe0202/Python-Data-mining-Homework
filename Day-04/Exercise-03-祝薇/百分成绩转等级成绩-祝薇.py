a=float(input("your test scores:"))
if a>=0 and a<60:
    print("Level D")
elif a<75:
    print("Level C")
elif a<85:
    print("Level B")
elif a<100:
    print("Level A")
else:
    print("Error")
