l1=[108,109,110,111]                    #it is 
print("1",l1)                           #    ->sequence type,
print("2",l1[1])                        #    ->square brackets
a=l1[2]                                 #    ->CHANGEABLE 
print("3",a)                            #    ->stored any type of data[1,"d",0.5,"thiru"]
print("4",l1[-4])
l2=["thiru",0,1.5,a]                        # id -> memory location ,type-> type of input
print(type(l2[3]))

a=["thiru",3,"sns",5]
b=[3,"neshak",5,"college"]
#print(a.clear())
print(a.copy())
print(a.count(3))
print(a.index(5))
print(len(a))
#print(max(a))   #only all are same type
#print(min(a))
print(a.pop(0)) #remove using index
print(a)
a.remove(3) #remove using value
print(a)

a.insert(0,"thiru")                            #  insert               append            pop       remove
a.insert(1,3)                                  # (index,value)        (value)           (index)    (value)
print(a)                                       #  for adding          for adding

a.append("eng")
a.append("e")
print(a)

a.extend(b)   #-> to join both list
print(a)

c=list("thiru")
print(c)
c.sort()
print(c)
c.sort(reverse=True)
print(c)

d=["book","is","mines"]
d.sort(key=len)
print(d)
print(d)


