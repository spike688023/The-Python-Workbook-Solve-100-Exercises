#Print out the last name of the second employee
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

print(d['employees'][1]['lastName'])


"""
這題要注意的是, 型態, 

有 : 在的那區塊, 是字典, 很好認, 

但如果要每個區塊, 都用肉眼, 一個個符號看,  太傷了, 

所以, 用type, 來看目前的型態, 這樣比較清楚.


不然先用肉眼看, 早就瞎了.
>>> d["employees"]
[{'lastName': 'Doe', 'firstName': 'John'}, {'lastName': 'Smith', 'firstName': 'Anna'}, {'lastName': 'Jones', 'firstName': 'Peter'}]
>>> type(d)
<class 'dict'>
>>> type(d["employees"])
<class 'list'>
>>> d["employees"][1]['lastName']
'Smith'

"""
