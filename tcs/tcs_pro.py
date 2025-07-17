'''n=input("enter the numbers:")
temp=1
for i in n:
    a=temp*int(i)
    temp=a
print(temp)'''

def price(n):
    temp=1
    for i in n:
        a=temp*int(i)
        temp=a
    return temp
n=input("enter the number:")
res=price(n)
print(f"the price is{res} ")

