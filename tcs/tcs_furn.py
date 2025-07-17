'''#try--1
b=int(input("Size of the box:"))
colour=list(str(input("enter the curtain colour have in factory (a-aqua / b-black):").split(len(3))))
print(colour)
#try--2
n=input("enter:")
n1=[]
for i in n:
    a=str(i)
    n1.append(a)
print(n1)'''

'''colour=list(input("enter the curtain colour have you want(a-aqua)/(b-black):"))
b=int(input("enter the size of bag:"))
max_a=0
max_group=""
max_group_index=0

g_index=1
for i in range(0,len(colour),b):
    g=colour[i:i+b]
    count_a=g.count('a')
    if count_a > max_a:
        max_a=count_a
        max_group=g
        max_group_index=g_index
    g_index+=1

print(max_a)
print(max_group)
print(max_group_index)'''

def furn(colour,b):
    max_a=0
    max_group_name=""
    max_group_index=0
    max_group_number=1
    for i in range(0,len(colour),b):
        g=colour[i:i+b]
        count_a=g.count("a")
        if count_a > max_a:
            max_a=count_a
            max_group_name=g
            max_group_index=max_group_number
        max_group_number+=1
    print(f"the maximum A occur is {max_a}")
    print(f"the maximun A occur group is {max_group_name} ")
    print(f"the maximum A occur group index is {max_group_index} ")
colour=list(str(input("enter the colours avaiable (a-aqua/b-black):")))
b=int(input("enter the size of the bag:"))
furn(colour,b)
