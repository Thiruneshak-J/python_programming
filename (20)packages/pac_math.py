import math as m

#math constants(3)
print(m.pi)
print(m.e)
print(m.tau)
#sqrt(5)
print("sqrt",m.sqrt(4))
print("gcd",m.gcd(45,54,14))
print("lcm",m.lcm(45,54,14))
print("maximun float number(ceil)",m.ceil(1.5)) #convert max number 1.5 --> 2
print("mininmum foat numbe r(floor)",m.floor(1.5)) #convert min number 1.5 -->1

#factorial(2)
print(m.factorial(5))
print(m.fabs(5))      # | both as
print(m.fabs(-5))     # | to make negative or positive as positive float

#fsum,pow,prod,comb,perm (5)                                           BOTH operations are SAME
print(pow(890,5))     #-->integer                                   m.pow(a,b)      |    pow(a,b)
print(m.pow(890,5))   #-->float                                     --------------------------------
print(890**5)         #--->                                         float           |     int
                      #-->                                          more accurate   |   accurate
print(pow(890,5))
print(m.fsum((45,45,45)) )                              # BOTH operations are SAME
print(m.prod((3,2)))                                    #   m.fsum,m.prod     |     sum,*
print("combination:",m.comb(20,4))                      #-----------------------------------------
print("permutation:",m.perm(20,4))                      # more accurate       |  accurate             
                                                        # float               |   int
                                                        # only iteable(),[]   |    single value   
#cd(2)
print(m.copysign(-5,9))
print(m.dist((2,0),(0,3)))

#reminder  (2)          
print(m.remainder(5,4))  #closedt value   
print(m.fmod(5,4))      # reminder                 

#degrees & rad (2)
print(m.degrees(5))
print(m.radians(45))
                                                        
                                                        

#copy sign works
#|||||||||||||
#`````````````
def  cp(x,y):
    if y>0:
        return abs(x)*1.0
    else:
        return -abs(x)*1.0
x=int(input("enter the x value:"))
y=int(input("enter the y value:"))
print(cp(x,y))

#fsum works
num=list(map(int,input("enter the number").split(" ")))
for i in num:
        pass   #or continue
print(sum(num))   
print(m.fsum(45,45,45)) 

#Alternative fsum works
n=[]
while True:                 
    v=input("enter the numebers")
    if v=="":
        break
    n.append(int(v))
print("sum:",m.fsum(n))

n=m.factorial(20)
r=m.factorial(4)
M=m.factorial(16)
print(n/M)