#Create a function like in the previous exercise, but taking into consideration that commas without space can separate words.
def count_words(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string = string.replace(",", " ")
        string_list = string.split(" ")
        return len(string_list)

print(count_words("words2.txt"))

#Other solution using regular expressions
import re

def count_words_re(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string_list = re.split(",| ", string)
        return len(string_list)

print(count_words_re("words2.txt"))


"""
我修改 36.py , 藉由去計算 , 的數目, 把回傳值加上這個數目, 

就是題目要的, 因為一個字裡面有出現幾個,   這個字, 就會再多切割出幾個來,

abc,cde,bbb 

這個答案的第二個方式,

在於re module中, 能吃多個分隔字元
"""
