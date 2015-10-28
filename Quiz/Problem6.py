def count7(N):
    """
    N: a non-negative integer
    Returns: number of times 7 appears in integer
    """
    global x
    global a
    try:
        x=x
        if len(str(N))!=x:
            a=0
        else:
            a=a
    except NameError:
        a=0

    if N==0:
        #print "shouldn't change"+str(a)
        global b
        b=0
        return a

    elif N%10==7:
        a=a+1
        #print 'this should increase'+str(a)
        N=N/10
        x=len(str(N))
        count7(N)
    elif N%10!=7:
        #print 'run with one less digit'+str(a)
        N=N/10
        x=len(str(N))
        count7(N)
    global b
    b=0
    return a