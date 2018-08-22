import turtle as t

def kehe(n,long):
    if n==0:
        t.fd(long)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            kehe(n-1,long/3)



for i in range(3):
    kehe(3,200)
    t.right(120)
