def simple_intrest(principal,intrest,time):
    return (principal*intrest*time)/100

if__name__=="__main__":
    p = int(save.Argv[1])
    i = float(save.Argv[2])
    t = int(save.Argv[3])

    print("Simple intrest is:",simple_intrest(p,i,t))