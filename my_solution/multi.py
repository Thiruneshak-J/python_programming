while True:
    try:
        n=int(input("enter the number to make multiplication table:"))
        if n<=0 :
            exit()
        t=int(input("number of times to make the table:"))
        if t<=0 :
            exit()
        for i in range(1,t+1):
            m=n*i
            print(f"{i} * {n} = {m}")
        print("thankyou")
    except ValueError:
        print("you entered alpabet")
        exit()
    