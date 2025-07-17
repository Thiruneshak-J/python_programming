def pali(a):
    org=a
    rev=0
    while(a!=0):
        rem=a%10
        rev=rev*10+rem
        a//=10
    if org==rev:
        return "it is palindrome"
    else:
        return "not a palindrome"
a=int(input("enter the number:"))
res=pali(a)
print(res)

      