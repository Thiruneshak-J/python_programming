'''start=input("enter the day of starting:").lower()
total=int(input("how many days between:"))
days=["sun","mon","tue","wed","thu","fri","sat"]
start_index=days.index(start.lower())
c=0
for i in range(total+1):
    cur=days[(start_index+i)%7]
    if cur=="sun":
        c+=1
print(c)
'''
def count_sun(start_day,total_day):
    days=["sun","mon","tue","wed","thu","fri","sat"]
    start_day_index=days.index(start_day.lower())
    c=0
    for i in range(total_day+1):
        cur=days[(start_day_index+i)%7]
        if cur=="sun":
            c+=1
    return c
start_day=input("enter the 1st date day:").lower()
total_day=int(input("enter the days to find how many sundays between:"))
res=count_sun(start_day,total_day)
print(f"there are {res} sundays between {total_day}")