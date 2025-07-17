n=int(input("enter the number of vehicles: "))
veh=[int(input("enter the vehicle number:")) for i in range(n)]
#or --->   veh=list(map(int,input("enter the vehicles numbers(by comma): ").split(",")))
val_d=int(input("enter the value of date :"))
fine=int(input("enter the fine amount:"))
if len(veh)!=n:
    print(f"number of vehicles are {n}, you entered vehicle numbers {len(veh)}")
else:
    if 0 < n <=100 and 1 <= val_d <= 30 and  100 <= fine <=5000:
        if val_d%2==0:
            odd_v=[]
            for i in range(0,len(veh)):
                if veh[i]%2!=0:
                    odd_v.append(veh[i])
            ans=len(odd_v)*fine
            print(ans)
        elif val_d%2!=0:
            even_v=[]
            for i in range(0,len(veh)):
                if veh[i]%2==0:
                    even_v.append(veh[i])
            ans1=len(even_v)*fine
            print(ans1)
    else:
        exit
            

    