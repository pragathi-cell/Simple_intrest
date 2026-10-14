def simple_intrest(principal,intrest,time):
    return (principal*intrest*time)/100

if__name__=="__main__":
    p = int(input("Enter principal amt"))
    i = float(input("Enter intrest"))
    t = int(input("Enter time in months"))

    print("Simple intrest is:",simple_intrest(p,i,t))