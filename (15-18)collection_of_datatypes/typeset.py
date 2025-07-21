a={1,2,3,4,"t"}
b={6,7,8,9,"t"}
a.add(7)                  #add -> adding less values any type
a.update("a","y","t")     #update -> adding more values only "str"
a.remove("a")             #only one
a.pop()                    # delete last enter value
a.clear()
a={1,2,3,4,"t",6,7,8,9}
print(a,b)

print(a.union(b))
print(a|b)

print(a.intersection(b))
print(a&b)

print(a.symmetric_difference(b))
print(a^b)
print(a-b)
print(b-a)

#update
'''a.intersection_update(b)
a.symmetric_difference_update(b)
print(a)'''
print(a)
print(b)
print(a.isdisjoint(b))
print(b.issubset(a))   #b is inside a
print(a.issuperset(b)) #both are same
