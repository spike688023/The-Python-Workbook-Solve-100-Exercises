#Add a new employee to the dictionary and print the dict out

from pprint import pprint

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))

pprint(d)


"""
我的寫法也是對的,  但是, 

上面的寫法, 也差不多拉.
>>> d["employees"].append({'firstName': 'Albert', 'lastName': 'Bert'})
"""
