#Store the dict to a json file

import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open("company2_indenct=2.json", "w") as file:
    json.dump(d, file, indent=2, sort_keys=True)
    #json.dump(d, file, indent=4)
    #json.dump(d, file)


"""
還真的有排板好, 我先來看 sort_keys , 這個會把dict結構的資料, 

依key做排序, vimdiff company2.json company1.json , 可以看出差異, 

dict內的key firstName lastName, 會把 firstName放第一個.

vimdiff company2.json company2_indenct\=2.json    ; 這個可以觀察, 內縮的差別.


我是用, help(json) , 這裡面的一段, 取出來用, 

把輸出變的跟題目要的很像, 但忘了,  要存入檔入內, 

我很懷疑, 上面的參數, 存入json file中, 就會有好的排板了嗎?

    Pretty printing::

        >>> import json
        >>> s = json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4)
        >>> print('\n'.join([l.rstrip() for l in  s.splitlines()]))
        {
            "4": 5,
            "6": 7
        }

"""
