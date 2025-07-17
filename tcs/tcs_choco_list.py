pac=int(input("enter the size of packet:"))
n=list(map(int,input("enter the numbers(by comma):").split(",")))
fin=[]
if len(n)!=pac:
    print(f"you entered {len(n)},but packet size is {pac}")
else:
    for i in range(0,len(n)):
        if n[i]!=0:
            fin.append(n[i])
    for j in range(0,len(n)):
        if n[j]==0:
            fin.append(n[j])
    print(n)
    print(fin)




