#Like the previous exercise, but returning a message when the word is not in the dict.
d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "That word does not exist."

word = input("Enter word: ")
print(vocabulary(word))

"""
哈， 別堂課有寫過類 似的， 它是藉由判斷  Error ，來做相對應的處理，

但這還要知道，Error 是那一類的, 以執行 速度上來看，它的比較快，

因為我的還要比過所 有的list ，它只要比沒有， 就算是Error了。
if word in d.keys():
        print(vocabulary(word))
        else:
            print("We couldn't find that word!")


好，它會表達給 你知道，這是什麼Error
>>> d = dict(weather = "clima", earth = "terra", rain = "chuva")
>>> d["fasdfsaf"]
Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      KeyError: 'fasdfsaf'
"""
