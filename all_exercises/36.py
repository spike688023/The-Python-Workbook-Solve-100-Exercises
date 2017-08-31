#Create a function that takes a text file and returns the number of words
def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)


def count_words2(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        print("strng.count(',') = " + str(strng.count(',')))
        return len(strng_list) + strng.count(',') 

print(count_words("words1.txt"))


print(count_words2("words2.txt"))
"""

open(words,r) 這是我一開始的使用方式, 印像中是對的, 

              但我犯了一個錯, 那就是 沒給雙引號, 或字元給單引號, 會被視為是變數

還有的就是下面是open func的定義, 每個參數都有接的變數, 我在用的時侯, 

有給  或沒給, 是沒差的, 只差在可讀性而己, 我覺得.

open(...)
    open(file, mode='r', buffering=-1, encoding=None,
         errors=None, newline=None, closefd=True) -> file object

    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (for backwards compatibility; unneeded
              for new code)
    ========= ===============================================================


這是我自己實作的, 我想功能一樣, 只是差在 input的文檔不一樣,

我有的元素是'' , 因為 我字跟字中間, 有時會有二個空白, 

而下面輸出的二個例子, 只有差在最後面, \n 有跟前面合在一起還是分開, 

這個差別在於, 最後一個字後面,有沒有空白, 把它跟換行字符隔開來.
['fsa', '', 'fsf', 'sd', 'fsd', 'f', 'sf', 'asf', 's', 'fs', '', 'fa', 'f', 's\n']
14

['fsa', '', 'fsf', 'sd', 'fsd', 'f', 'sf', 'asf', 's', 'fs', '', 'fa', 'f', 's', '\n']
15


"""
