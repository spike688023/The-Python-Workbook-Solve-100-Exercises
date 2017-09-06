#Add the missing items to the file
"""
概念一樣, 但我list的串接是用  append , 

python 很多東西, 都能用運算子去實作, 但我很少用.
"""

checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + "\n" for i in checklist]

with open("countries_missing.txt", "r") as file:
    content = file.readlines()
print(checklist + content)

updated_list = sorted(checklist + content)

with open("countries_missing_fixed.txt", "w") as file:
    for i in updated_list:
        file.write(i)
