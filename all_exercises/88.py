#Create a script that uses countries_by_area.txt file as data sourcea and prints out the top 5 most densely populated countries
"""
有些寫法，跟我不太一樣，但整體來說，

是一樣的，

每一個column的取用，跟字典是一樣的。

那一個row呢，喔， 用values() 嗎？ data[:5]  用list

作者多用了個iterrows() ，這個會比我原本的方便，

"""

import pandas

data = pandas.read_csv("countries_by_area.txt")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)

for index, row in data[:5].iterrows():
    print(row["country"])
