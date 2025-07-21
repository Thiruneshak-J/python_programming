while True:
    w=int(input("enter the number wheels:"))
    v=int(input("enter to manufacture the vehicles with wheels:"))
    if (w&1)==1 or w<2 or w<=v:
        print("INVAILD OUTPUT")
    else:
        fw = (w-2*v)//2
        tw = v-fw
        print("TW",tw)
        print("fw",fw)
        print("Two Wheelers={0}\n four Wheelers={1}".format(tw,fw))
        ch=input("another cal(y/n):").lower()
        if ch!="y":
            break