"""
這題要搞清楚的就是,  東西什麼時侯在memroy , 什麼時侯, Disk

tell()¶
Return the current stream position.
"""
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

file = open("97_writting.txt","w+")
while True:
    userinput = input("Write a value:")
    for case in switch(userinput):
        if case("CLOSE"):
            break
        if case("SAVE"):
            file.flush()
        if case():
            file.write(userinput+"\n")            
    if userinput == "CLOSE": break
            

file.close()
