import array as ar
'''
n=int(input("enter the size of array:"))
arr=map(int,input("enter the numbers(by comma) : ").split(","))
arr1=ar.array('i',arr)
if len(arr1)!=n:
    print(f"the array size is {n},you entered {len(arr1)}")
else:
    for i in range(0,len(arr1)-1):
        for j in range(i+1,len(arr1)):
            if arr1[i]>arr1[j]:
                temp=arr1[i]
                arr1[i]=arr1[j]
                arr1[j]=temp
    print(arr1)'''


def air(arr1):
    if len(arr1)!=n:
        print(f"the array size is {n},you entered {len(arr1)}")
    else:
        for i in range(0,len(arr1)-1):
            for j in range(i+1,len(arr1)):
                if arr1[i]>arr1[j]:
                    arr1[i],arr1[j]=arr1[j],arr1[i]
        return arr1
n=int(input("enter the size of array:"))
arr=map(int,input("enter the nummber(seperated by comma:)").split(","))
arr1=ar.array('i',arr)
res=air(arr1)
print(f"security purpose result is {res}")

        