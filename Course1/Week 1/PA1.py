def Karatsuba(x, y):
    n = min(len(str(x)), len(str(y)))
    #print("n: ", n)
    #if n%2 == 1 and n!=1:
    #    print("n is odd: ", n)
    #    print("len(x): ", len(str(x)), " and x: ", x)
    #    print("len(y): ", len(str(y)), " and y: ", y)
    if n==1:
        return x*y
    t = n//2
    #print("t: ", t)
    a = x//(10**(t))
    #print("a: ", a)
    b = x - (a*(10**t))
    #print("b: ", b)
    
    c = y//(10**(t))
    #print("c: ", c)
    d = y - (c*(10**t))
    #print("d: ", d)
    ac = Karatsuba(a, c)
    #print(ac)
    apbcpd = Karatsuba(a+b, c+d)
    #print(apbcpd)
    bd = Karatsuba(b, d)
    #print(bd)
    adpbc = apbcpd - ac - bd
    return (10**(2*t))*ac + (10**t)*adpbc + bd


#print(Karatsuba(80056470, 42533735))
#Ans:3405100680015450

#x = 3141592653589793238462643383279502884197169399375105820974944592
#y = 2718281828459045235360287471352662497757247093699959574966967627
#print(Karatsuba(x, y))


#print(Karatsuba())
#print(Karatsuba(2, 3))
#print(Karatsuba(1234, 5678))
#print(Karatsuba(12, 12))

