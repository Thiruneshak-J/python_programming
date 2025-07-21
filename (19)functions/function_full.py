#functions
def wel():
    print("example : hi! i am thiru")
wel()


    #there are four types of function
    #->user-defined function
    #->bulit in function
    #->lambda function
    #->recursion functoin'''
#There are nine types of user-defined function like                         return                              print
    #  1-no arguments and no return func                            return used in function                 print which is display what
    #  2-no arguments and return func                               which send back the process              we except to the console   
    #  3-arguments and no return func                               to the caller or func                      or output
    #  4-arguments and return func
    #  5-arbituary argument func
    #  6-keyword arguments func
    #  7-arbituary keyword argument func
    #  8-default parameter func
    #  9-arguments as list in func

#----->user-defined function
#  1-no arguments and no return func  
def add():
    a=10
    b=12
    c=a+b
    print("1",c)
add()

#2-no arguments and return func 
def sub():
    a=10
    b=20
    c=b-a
    return c
res=sub()  #object for a function
print("2",res) #or print(sub())

# 3-arguments and no retun func
def mul(a,b):
    c=a*b
    print("3",c)
mul(10,2)

# 4-arguments and return func
def div(a,b):
    c=a/b
    return c
res=div(4,2) #ob
print("4",res)  # or print(div(6,3))

# 5-arbituary arguments func
def class1(*std):
    for i in std:
        print("5",i)
class1("thiru","sns","finalyear")

def class2(*std):
    return std
print(class2("5(1)-thiru","sns","finalyear"))

# 6- keyword arguments func
def det(name,age):                                                              #if keyword function occures we shoud not use
    print("6",name,"age is",age)                                                                      #return only use print
det(name="thiru",age=21)

# 7 - arbitaury keyword func
def bio(**data):
    return data
res=bio(name="ram",age=21,gender="male",city="theni")
print("7",res)

# 8-default parameter
def info(name,city="theni"):
    print("8",name,"is from",city)
info("thiru","madurai")
info("thiru")

# 9- arguments as list
def test(mark):
    return sum(mark)
res=test([10,20,30,40])
print("10",res)


#---->lambda function
c=lambda a:a+50
print(c(5))

#----->recursive function
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
print("fact",fact(5))
