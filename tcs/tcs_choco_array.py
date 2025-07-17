import array as ar
pac=int(input("enter the packet size:"))
n=map(int,input("enter the numbers(seperated my comma):").split(","))
ch=ar.array('i',n)
fin=ar.array('i',[])
if len(ch)!=pac:
    print(f"you entered {len(ch)},but packet size is{pac}")
else:
    for i in ch:
        if i!=0:
            fin.append(i)
    for i in ch:
        if i==0:
            fin.append(i)
print(ch)
print(fin)




