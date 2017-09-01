#The script is trying to print out the type of the last character of updated string.
#A: One more bracket is needed to close the print function
print(type("Hey".replace("ey","i")[-1]))


"""
SyntaxError: unexpected EOF while parsing

原來少一個右括, 會有這種訊息, 因為在做parse時, 

它期待還會讀到一個右括, 但卻沒有出來.
"""
