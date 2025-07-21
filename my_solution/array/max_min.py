import array as ar
while True:
    num=int(input("enter the size of array:"))
    n1=[int(input("enter the number:")) for _ in range(num)]
    n=ar.array('i',n1)
    print("you enterd elements are :",n)
    ch=int(input("enter the choice (1-find max) (2-find min):"))
    if ch==1:
        temp=0
        for i in range(0,len(n)):
            if n[i]>temp:
                temp=n[i]
        print("maximum element in array is :",temp)
    elif ch==2:
        temp1=n[0]
        for j in range(0,len(n)):
            if n[j]<temp1:
                temp1=n[j]
        print("minimum element in array is :",temp1)
    con=input("do you run agian(y/n):").lower()
    if con=="y":
        continue
    else:
        break

