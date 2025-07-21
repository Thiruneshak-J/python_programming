
'''def div(a,b):
        c=a/b
        return c
a=int(input("enter the number:"))
b=int(input("enter the number:"))
try:
     divi=div(a,b)
except Exception as e:
    print(e)
else:
    print("divion of a,b=",divi)
try:
    division=div(7,0)
except Exception as e:
    print(e)
else:
    print("the second answer is",division)
finally:
    print("thnakyou")'''
#types of exception
#print(dir(locals()['__builtins__']))
#print(len(dir(locals()['__builtins__'])))
try:
    f=open("(1,2,3,4)readme python.txt","r")
except FileNotFoundError:
    print("file is not found")
try:
    f=open("lcm_gcd","w")
except PermissionError:
    print("no permission")
#filenotfound error
#permission error
#isadirtectory error
#i/o error or oserror
#unsupportedoperation error
