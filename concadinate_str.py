# a="apple"
# b="orange"
# c=0
# s=a+b
# print(s)
# r=""
# for i in s:
#     if i not in r:
#         r=r+i
# print(r)

# a=[21,32,12,32,12,21,21]
# print(sorted(a))


# for i in sorted(r, reverse=True):
#     print(i,end=" ")

str1=input()
str2=input()

s= str1+str2
n_str=""

for ch in s:
    if ch not in n_str:
        n_str+=ch
chars=list(n_str)

for i in range(len(chars)):
    for j in range(i + 1, len(chars)):
        if chars[i]<chars[j]:
            chars[i],chars[j]=chars[j], chars[i]

res=""
for ch in chars:
    res+=ch

print(res)
