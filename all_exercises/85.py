#Create a script cleans the countries_raw.txt file from unecessary lines and leaves countries only

with open("countries_raw.txt", "r") as file:
    content = file.readlines()

# 用 \n 去分類, 用list裝
content = [i.strip("\n") for i in content if "\n" in i]

# 這徰很奇怪, 它是代表空字串, 不是換行符號 
# 只能猜, 是上面用\n的分割方式, 有我沒想到的case
content = [i for i in content if i !=""]

# 這很明顯是拿走  有 Top of Page的行
content = [i for i in content if i !="Top of Page"]

content = [i for i in content if len(i) != 1]
print(content)


with open("countries_clean.txt", "w") as file:
    for i in content:
        file.write(i+"\n")
