'''user={"name":"thiru",
      "age":21,
      "city":"theni"}
print(user)
print(user["name"])
print(user.get("name"))
print(user.keys())
print(user.values())
print(user.items())

user.update({"blood group":"B+ve"})
print(user.keys())
print(user.items())

user["age"]=22
print(user.get("age"))

for x in user:            #1st loop ( x ) defines its keys -> default loop as keys
    print(x," ",user[x])

for k in user.keys():
    print(k)

for y in user.values():
    print(y)

for x in user:
    print(x) #or print(user[x])

for x,y in user.items():
    print(x,y)'''

users={"user1":{"name":"thiru","age":22,"city":"theni"},
       "user2":{"name":"neshak","age":21,"city":"bodi"}
}
print(users)
users.update({"user3":{"name":"jaya","age":"49"}})
print(users)
print(users.keys())
print(users.values())