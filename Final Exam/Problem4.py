# Part 1
def getSublists(L, n):
    """
    Function that returns all sublists of list L with length n. 
    All sublists do not skip elements of L.
    """
    result=[] #final output list
    for i in range(len(L)-n+1):
        temp=L[i:i+n]
        result.append(temp)
    return result

#Part 2
def longestRun(L):
    """
    Function that returns the length of longest sublist in L with all 
    elements in increasing monotonic order. 
    """
    for i in range(len(L),0,-1):
        sublists=getSublists(L, i)
        for j in range(len(sublists)):
            result=True
            list=sublists[j]
            for q in range(len(list)-1):
                if list[q]> list[q+1]:
                    result=False
            if result==True:
                output=i
                return output
    