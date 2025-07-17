import random as r
print(r.random())
print(r.randint(1,10))
print(r.uniform(1,10))
print(r.randrange(0,10,2))
print(r.randrange(1,10,2))

a=["apple","banana","carrot","dragonfruit"]
print(r.choice(a))
print(r.choices(a,k=5)) #its may generates also duplicate , we can also enter k value above of list
print(r.sample(a,k=2))  #its only generates unqiue        , we can enter only within k value

b=[1,2,3,4,5]
print(b)
r.shuffle(b)
print(b)

r.seed(9.0)
print(r.randint(1,100))