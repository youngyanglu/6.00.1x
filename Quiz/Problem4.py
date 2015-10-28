#Part 1

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    y=a*x**2+b*x+c
    return y
    
#Part 2
def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    a=evalQuadratic(a1,b1,c1,x1)
    b=evalQuadratic(a2,b2,c2,x2)
    print a+b
    
           