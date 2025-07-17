t="thiruneshak"                                                    #----->
print("1",t)        # 1 -> whole string                          0 1 2 3 4 5 6 7 8 9 10
                                                                #T h i r u n e s h a k   [0:2] stop stops from previous of given index
#positive                                                      -11-10-9-8-7-6-5-4-3-2-1        start starts with given index itself
print("2",t[:])    #-> whole string                                             <-------
print("3",t[0:2])  #-> 1st two
print("4",t[:5])    #-> print index of 0,1,2,3,4
print("5",t[3:])    #-> print index of 3 till last
print("6",t[1:5])   #-> print index 1 to 4

#negative
print("7",t[-1])
print("8",t[-2:-1])
print("9",t[:-1])
print("10",t[-3:])


#using ::
print("11",t[::2])
print("12",t[::-1])  #-> reverse string
print("13",t[::-2])  #->from back print by leave 2 by 2 (oppo of 11)
print("14",t[1::2])

#start,stop,step
print("15",t[5:2:-1])
print("16",t[0:5:2])