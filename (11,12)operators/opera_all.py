'''#arthmetic operators
a=22
b=2
print("addition=",a+b)
print("subtraction=",a-b)
c=a*b
print("multipulication=",c)
print("divison=",a/b)
print("modules Or remainder=",a%b)
print("floor divison Or Quoitent=",a//b)
print("exponentation=",a**b,"altermethod=",(pow(a,b)) )

#assignment operator
a=40
a+=10
print(a) #50
a-=5
print(a) #45
a*=2
print(a) #90
a/=5
print(a) #18

def assign(a):
        a+=10
        print(a)
        a-=5
        print(a)
assign(40)

#comparison or relational operator
def relation(a,b):
        c=(a==b)
        print(c)
        c=(a!=b)
        print(c)
        c=(a>=b)  
        print(c)              
        c=(a<=b)
        print(c)
        c=(a<b)
        print(c)
        c=(a>b)
        print(c)
r=relation(10,20)

#logical opertor
while True:
        a=int(input("enter the number:"))
        b=int(input("enter the number2:"))
        if a>b and a==b:
                print("a is greater and greater then = b")
        elif b>a and b==a:
                print("b is greater and greater then =a")
        elif a==b or a>b:
                print("a=b or a>b")
        elif a==b or b>a:
                print("a==b or b>a")
        elif a not in b:
                print("a!=b")
        else:
                print("sorry")
        ch=input("do you want to continue(yes/no):").lower()
        if ch != "yes" :
                break
'''
#bitwise operator
a,b="10,5".split(",")
a,b=int(a),int(b)                                                                                    #print bin to orginial number
print("10=",bin(a),"5=",bin(b))
print(a&b) #to show only 1 and 1 = 1 -> T + T =T print(adding of true value)   
print(a|b) #to show only 0 and 0 =0 -> F + F = F print(adding of true value->1111->8+4+2+1=15)
print(a^b) #if same = 0 ,if different = 1 -> t,t=0___f,f=0 but t,f=1 __f,t=1 print(adding of true value->1111->8+4+2+1=15)
print(~a) #it will opposite if 0 then 1 ,if 1 then 0 




    
        

