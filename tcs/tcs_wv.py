v=600000
w=100000
if (w&1)==1 or w<2 or w<=v:
    print("INVALID INPUT")
else:
    x=((4*v) -w)//2
    print("TW={0} FW={1}".format(x,v-x))