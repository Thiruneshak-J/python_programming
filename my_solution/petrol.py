today_price=102.11
total_lit=5000
def lit(l):
    global total_lit
    a=l*today_price
    print(f"the litres you want {l}\n , for that amount is {a}")
    total_lit-=l
    print("``````````````````````~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~```````````````````````````````````````````")
    print("remaining litres in bluck is ",format(total_lit,".2f"))
def amount(a):
    global total_lit
    li=a/today_price
    print(f"the amount you given {a}\n","the litres you get",format(li,".2f"))
    total_lit-=li
    print("``````````````````````~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~```````````````````````````````````````````")
    print("remaining litres in bluck is ",format(total_lit,".2f"))
print("1-enter the amount:\n"
      "2-enter the litre/litres:\n"
      "3-exit")
while True:
    ch=int(input("choose the digit (amount-1)(litre-2)(exit-3)"))
    if ch==1:
        a=int(input("enter the amount:"))
        amount(a)
    elif ch==2:
        l=float(input("enter the litre/litres:"))
        lit(l)
    elif ch==3:
        print("exiting........")
        break
    else:
        print("invaild option try again")
        

