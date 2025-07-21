for i in range(4):               #-->     ********
    for j in range(8):                  # ********
       print("*",end="")                # ********    
    print()                             # ********

for i in range(3,0,-1):           #--> ***
        for j in range(i):           # **
            print("*",end="")        # *
        print()
r=5
for i in range(r):
    for j in range(r - i + 1):                                          #           *
        print(" ", end="")  # Print leading spaces                      #          * *
    for k in range(2 * i + 1):                                          #         *   *
        if k == 0 or k == 2 * i or i == r-1:                            #        *     *
            print("*", end="")  # Print star at boundaries or bottom row        *********
        else:
            print(" ", end="")  # Print space inside
    print()


r=5
for i in range(r):                  #->1
    for j in range(i):                #12
        print(j+1,end="")              #123  
    print()                             #1234

r=5
for i in range(r):
    for j in range(i):                                      # *********
        print(" ",end="")                                   #  *     *
    for k in range(r - i + 4):                              #   *   *
        if  k == 0 or k == 4 * 2 - i * 2 :                  #    * *
            print("*",end="")                               #     *
        elif i == 0 :
            print("*",end="")
        else:
            print(" ",end="")
    print()

n=5 
for i in range(n):                      #--> ******
    for j in range(n):                  #    *
        if i==0 or i==4 or j==i: #j=0   #    *
            print("*",end="")           #    *
    else:                               #--> ******
        print(" ",end="")
    print()

n=5
for i in range(n):
    for j in range(9):                          # *
        if i == 4 or j==0 or j ==2*i:           # *  *
            print("*",end="")                   # *   *
        else:                                   # *     *
            print(" ",end="")                   # ********
    print()