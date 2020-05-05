n = int(input("num:"))
for i in range(2, n):
    if n%i==0:
        print("N")
        break
else:
    print("Y")
