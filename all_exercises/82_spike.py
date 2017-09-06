"""
這裡的.是當目録的意思。
from .formats import *

這裡的意思，應該 是指，在module astropy的目録下，
的folder，

PACKAGE CONTENTS
    _compiler
    _erfa (package)
    analytic_functions (package)
    config (package)
    conftest
    constants (package)
    convolution (package)
    coordinates (package)
    cosmology (package)
    cython_version
    extern (package)
    io (package)
    logger
    modeling (package)
    nddata (package)
    samp (package)
    setup_package
    stats (package)
    table (package)
    tests (package)
    time (package)
    units (package)
    utils (package)
    version
    visualization (package)
    vo (package)
    wcs (package)

要記住一點，能被import 的，一定class function 或變數之類的。
這樣就 能解理 from xxx.xxx import *   就是把下面的所 有東西都載 進來，太多了。
>>> dir(astropy.time)
['OperandTypeError', 'ScaleValueError', 'TIME_DELTA_FORMATS', 'TIME_DELTA_SCALES', 'TIME_FORMATS', 'TIME_SCALES', 'Time', 'TimeBesselianEpoch', 'TimeBesselianEpochString', 'TimeCxcSec', 'TimeDatetime', 'TimeDecimalYear', 'TimeDelta', 'TimeDeltaFormat', 'TimeDeltaJD', 'TimeDeltaSec', 'TimeEpochDate', 'TimeEpochDateString', 'TimeFITS', 'TimeFormat', 'TimeFromEpoch', 'TimeGPS', 'TimeISO', 'TimeISOT', 'TimeInfo', 'TimeJD', 'TimeJulianEpoch', 'TimeJulianEpochString', 'TimeMJD', 'TimePlotDate', 'TimeString', 'TimeUnique', 'TimeUnix', 'TimeYearDayTime', 'TimezoneInfo', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'core', 'formats', 'utils']


這裡呢， 為什麼一定要先import ，才能用dir() 看它有什麼功能，

我想是田為pacakge folder裡面也有__init__.py ， 所以要先import ，

讓它先跑 這個檔案, 目前看來 from xxx.xxx import xxx 的這種 格式，

都是用來引入 package folder的 ，其它的只要單用import 即可。
>>> dir(astropy.coordinates)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: module 'astropy' has no attribute 'coordinates'
>>> import astropy.coordinates
>>> dir(astropy.coordinates)

弄錯  library 白忙一場。
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body_barycentric, get_body, get_moon , get_sun
t = Time("1230-01-01 00:00")
print("Sun")
print(get_body_barycentric('sun', t) )
#print( get_sun(t) )
print("Jupiter")
print( get_body_barycentric('jupiter', t) )
#print( get_body_barycentric('moon', t) )

終 於找到了，趁我病，要我命，超 多天的。
>>> help(mars)
 |  sun_distance
 |      distance from sun in AU
"""

from ephem import Jupiter
jupiter = Jupiter('1230/01/01')
#print(jupiter)
#print(jupiter.sun_distance)

#  哇操，轉換的值，跟它不一樣哎，
# 難怪我的答案跟它有點落差。
print(jupiter.sun_distance * 149597870.691)
