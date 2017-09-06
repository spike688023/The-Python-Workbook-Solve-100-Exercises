#Create a script that checks a list against countries_clean.txt
#and creates a list with items that were in that file

"""
好拉, 它這寫法,  要學一下, 把建立的條件都放在 [] 內.
"""

checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries_clean.txt", "r") as file:
    content = file.readlines()

content = [i.rstrip('\n') for i in content]
checked = [i for i in content if i in checklist]

print(checked)
