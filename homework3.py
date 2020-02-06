try:
    a=input("give the string to analyze")
    a = a.replace(" ","")
    b = 0
    c = 0
    d = 1
    e = a[0]
    for sign in a :
        if d > len(a)-1 :
            break
        if a[d] > a[d-1] :
            if b > c :
                b += 1
                c += 1
                e = e + a[d]
                f = e
            else:
                b += 1
                e =e + a[d]
        else:
            b = 0
            e = a[d]
        d += 1
    print ("the longer substring in alphabetical order is",f)
except :
    print("please  only use letter and space, at least 2 letter needed" )
