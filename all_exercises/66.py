#Create a function that takes a word from user and translates it using a dictionary of three words
d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    return d[word]

word = input("Enter word: ")
print(vocabulary(word))

"""

喔， 沒注意到題 目說要建一個function, 它網 頁上的 確實也沒有說。
>>> d = dict(weather = "clima", earth = "terra", rain = "chuva")
>>> print( d[input("Enter word:")] )

解 說的理由是  擴充性。
It's good to create a function as the above code shows so that the code is more organized in case you need to expand it and add more features later.
"""
