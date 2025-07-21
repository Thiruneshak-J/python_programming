'''n = int(input("how many data gointg to enter?"))
student_marks = {}
for i in range(n):
        name, *line = input("name:").split()      
        scores = list(map(float, line))
        student_marks[name] = scores
qn = input("average data name:")
avg=sum(student_marks[qn])/len(student_marks[qn])
print("average of given data is :{0:.2f}".format(avg))'''
'''n=[]
while True:
        a=input("enter the mark:")
        if not a.isdigit():
                break;
        m=int(a)
        if m<0:
                break
        else:
                n.append(m)
print(n)
to=sum(n)
av=sum(n)/len(n)
print(to)
print(av)'''

n=int(input("enter the number of subjects:"))
mark=[]
for i in range(n):
        s=int(input("enter the marks:"))
        mark.append(s)
print(mark)

