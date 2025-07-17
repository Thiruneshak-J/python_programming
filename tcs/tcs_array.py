import array as ar
'''n=int(input("enter the size of array:"))
arr=map(int,input("enter the array numbers(seperated by comma:)").split(","))
arr1=ar.array('i',arr)
m=[]
max=ar.array('i',m)
if len(arr1)!=n:
    print(f"the size of the array is {n}, you entered {len(arr1)}")
else:
    max.append(arr1[0])
    c=arr1[0]
    for i in range(1,len(arr1)):
        if (c < arr1[i]) :
            max.append(arr1[i])
            c=arr1[i]
    print(len(max))'''

def tcs_array(max1,arr1,n):
    if len(arr1)!=n:
        print(f"the size of array is {n},yoy entered {len(arr1)}")
    else:
        c=arr1[0]
        max1.append(arr1[0])
        for i in range(1,len(arr1)):
            if c < arr1[i]:
                max1.append(arr1[i])
                c=arr1[i]
        return max1
n=int(input("enter the size of array:"))
arr=map(int,input("enter the numbers(seperated by comma):").split(","))
arr1=ar.array('i',arr)
max1=ar.array('i',[])
res=tcs_array(max1,arr1,n)
print(len(res))

            

