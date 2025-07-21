n=int(input("enter the positive number:"))
m=(1<<n.bit_length())-1
t=n^m
print(t)