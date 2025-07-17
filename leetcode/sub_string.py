s=list(input("enter the string"))
out=[]
for i in range(0,len(s)):
    seen=[]
    for j in range(i,len(s)):
        if s[j] in seen:
            break
        seen.append(s[j])
    if len(seen)>len(out):
        out=seen
print(len(out))
