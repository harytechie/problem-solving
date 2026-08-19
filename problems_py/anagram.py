a="listen"
b="silent"
ch1=(list(a))
ch2=(list(b))
istrue=True
for i in ch1:
    if i not in ch2:
        istrue=False
if(istrue):
    print("Anagram")
else:
    print("not anagram")

