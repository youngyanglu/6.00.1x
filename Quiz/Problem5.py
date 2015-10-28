def primesList(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    a=[]
    b=range(2,N+1,1) 
    for int in b:
        for divisor in range(2,int,1):
            if int%divisor==0:
                a.append(int)
    c=[item for item in b if item not in a]
    return c      