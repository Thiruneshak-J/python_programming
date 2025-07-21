n=int(input("enter the number:"))
f=False
if n==1:
    print("neither prime nor composite number")
elif n>1:
    for i in range(2,n):
        if (n%i)==0:
            f=True
            break
    if f :
            print("not a prime number")
    else:
            print("prime number")