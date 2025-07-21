import array as ar
num=int(input("enter the size of array:"))
n1=[int(input("enter the number:")) for _ in range(num)]
n=ar.array('i',n1)
print("you enterd elements are :",n)
while True:
    pos=int(input("enter the index to insert:"))
    e=int(input("enter the element:"))
    num1=ar.array("i",[])
    for i in range(0,pos):
        num1.append(n[i])
    num1.append(e)
    for j in range(pos,len(n)):
        num1.append(n[j])
    n=num1
    print(f"the updated array is {num1}")
    ch=input("enter y/n:").lower()
    if ch!='y':
        break


