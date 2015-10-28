def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns a list of keys in aDict that map to integer values that are unique 
    The list of keys in increasing order. 
    If aDict doesn't have any unique values, returns an empty list.
    '''
    raw=aDict.values()
    clean = [ x for x in raw if isinstance(x,int) ]
    nodups = [x for x in clean if clean.count(x) == 1]
    aDictInv=dict((v,k) for k, v in aDict.iteritems())
    aDictInvclean= []
    for y in nodups:
        aDictInvclean.append(aDictInv[y])
    return aDictInvclean