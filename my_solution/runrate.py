'''input("enter the team name:")
temp=0
while True:
    for i in range(1,121):
        runs=int(input("runs scored:"))                       #addind while loop
        a=runs+temp
        temp=a
        rr=(a/i*120)/20
        print("runs=",temp , "balls=",i)
        print("runrate=",rr)
        if i%6==0:
            ch=input("contiue to next over(y/n):").lower()
            if ch != "y":
                break
'''

name=input("enter the team name:")
temp=0
overs=int(input("enter the overs:"))
o=overs*6
for i in range(1,o+1):
    runs=int(input("runs scored:"))
    a=runs+temp
    temp=a
    rr=((a/i)*o)/overs
    pj=(temp/i)*o
    print("runs",temp,"balls=",i , "projected score:",pj)
    print("runrate=",rr)
    if i%6==0:
        ch=input("if you want to continue (y/n):").lower()
        if ch!="y":
            break













