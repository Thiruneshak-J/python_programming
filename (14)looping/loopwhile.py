'''i=1
while i<=5:
    print(i,end="\n")
    i+=1
print()'''


'''
j=2
while j <=10:
    print(j,end=" ")
    j+=2
print()


k=1
while k<=10:
    print(k,end=" ")
    k+=2'''


'''num=[11,22,33,44,55,66,77,88,99]
i=0
while i<len(num):
    if num[i]==33:
        i+=1
        continue
    print(num[i])
    i+=1'''

'''num=[0,2,4,6,8,10]
i=0
while i<len(num):
    if i==2:
        i+=1
        continue
    print(num[i])
    i+=1

'''


''''num=[10,11,110,1210,422,522]
for i in range (len(num)):
    if num[i]==1210:
        continue
    print(num[i])'''

'''n=[0,1,4,3,4,5]
print(n[2])
if 2 in n:
    print("yes")
else:
    print("no")'''

'''n=["a","b","c","d"]
i=0
while i<len(n):
    if n[i]=="b":
        i=i+1
        break
    print(n[i])
    i+=1
'''
'''for i in range(0,10):
    if i==5:
        break
    print(i)
    '''
'''j=0
while j<10:
    if j==55:
        print(j)
        break
    j+=1
else:
    print("not is there")'''

for i in range(21):
    if i == 2:
        break
    print(i)
else:
    print("no")