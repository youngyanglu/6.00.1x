class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if atMe.name==newFrob.name:
        newFrob.setAfter(atMe.after)
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)

    elif atMe.name<newFrob.name:
        temp=atMe
        try:
            while temp.after.name < newFrob.name:
                temp=temp.after
            newFrob.setAfter(temp)
            newFrob.setBefore(temp.Before)
            temp.setBefore(newFrob)
        except AttributeError:
            newFrob.setBefore(temp)
            temp.setAfter(newFrob)

    elif atMe.name>newFrob.name:
        temp=atMe
        try:
            while temp.before.name > newFrob.name:
                #if temp doesn't have a before 
                #then means must have been smallest. So newFrob now smallest.
                temp=temp.before 
            newFrob.setAfter(temp.After)
            newFrob.setBefore(temp)
            temp.setAfter(newFrob)
        except AttributeError:
            newFrob.setAfter(temp)
            temp.setBefore(newFrob)


s = Frob('sterling')
r = Frob('rupert')
insert(s, r)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore() is not None:
        start=start.getBefore()
        findFront(start)
    return start.name


