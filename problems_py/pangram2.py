sen="thequickbrownfoxjumpsoverthelazydog"
word=(list(sen))
letter=96
istrue=True
while letter<122:
    letter=letter+1
    char=(chr(letter))
    if char not in word:
        istrue=False
        break
if(istrue):
    print("pangram")
else:
    print("not pangram")
