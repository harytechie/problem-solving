a="hi hello vanakkam"
ch=a.split()
r=ch[0]

for i in ch:
    if len(r)<len(i):
        r=i
print(r)