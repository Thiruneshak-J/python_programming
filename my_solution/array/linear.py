import array as ar
n1=list(map(int,input("enter the number:(by comma)").split(",")))
n=ar.array('i',n1)
print("you enterd element are ",n)
e=int(input("enter the element:"))
for i in range(0,len(n)):
    if n[i]==e:
        print("the index of your element is : ",i)
        print("the position is :",i+1)
