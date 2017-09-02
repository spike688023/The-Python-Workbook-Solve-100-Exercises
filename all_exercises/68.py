#Like the previous exercise, but considering user may enter different letter cases
d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "That word does not exist."

word = input("Enter word: ").lower()
print(vocabulary(word))


"""
做法，完全一樣，那就 不用特 別寫東西了。
"""
