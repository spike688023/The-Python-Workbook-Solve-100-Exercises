#Create a function that takes a string and returns the number of words
def count_words(string):
    string_list = string.split(" ")
    return len(string_list)

print(count_words("Hey there it's me!"))


"""
這裡一開始, 誤會了, 文意, 它是要一段字串內的words  ,

而不是要chars.
"""
