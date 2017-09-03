#Create a script that gets user's age and returns year of birth
from datetime import datetime

age = int(input("What's your age? "))
year_birth = datetime.now().year - age
print("You were born back in %s" % year_birth)

"""
from datetime import datetime

age = int(input("What's your age?"))
print(datetime.now())
print("You were born back in",datetime.now().year - age + 1)

"""
原來now 這個func會回傳 datetime object ，

難怪可以用year  month day 去取用。

>>> datetime.now
<built-in method now of type object at 0x106eec608>
>>> datetime.now()
datetime.datetime(2017, 9, 3, 16, 33, 24, 463544)
>>> help(datetime.now)

>>> help(datetime)

>>> datetime.now().year
2017


|  now(tz=None) from builtins.type
|      Returns new datetime object representing current time local to tz.
|
|        tz
|          Timezone object.
|
|      If no tz is specified, uses local timezone.
"""
