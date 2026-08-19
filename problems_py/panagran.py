a="The quick brown fox jumps over the lazy dog"
a1=a.lower()
ch=(list(a1))
ch1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
istrue=True
char=[]
for i in ch:
    if i!=' ':
        char.append(i)
for i in ch1:
    if(i not in char):
        istrue=False
        break
if(istrue):
    print("panagram")
else:
    print("not panagram")