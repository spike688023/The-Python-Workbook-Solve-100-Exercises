
import pandas
df = pandas.read_table("countries_by_area.txt",delimiter=',' )
df = df.assign(densely = lambda x: x.population_2013 / x.area_sqkm )
df = df.sort_values("densely", ascending=False)
topfive = [ i[1] for i in df.values[0:5] ]
for i in topfive:
    print(i)




"""
Pandas 真的超 方便的，

剛是read的種 類 就 有很多種了， 可以方便對，各種 資料做處 理跟擷取

'read_clipboard', 'read_csv', 'read_excel', 'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json', 'read_msgpack', 'read_pickle', 'read_sas', 'read_sql', 'read_sql_query', 'read_sql_table', 'read_stata', 'read_table',

這題 的重點在於，densely , 這個字， 我要藉由運算，去新 增一個column,

#|      >>> df.assign(ln_A = lambda x: np.log(x.A))
|          A         B      ln_A
|      0   1  0.426905  0.000000
|      1   2 -0.780949  0.693147
|      2   3 -0.418711  1.098612
|      3   4 -0.269708  1.386294
|      4   5 -0.274002  1.609438
|      5   6 -0.500792  1.791759
|      6   7  1.649697  1.945910
|      7   8 -1.495604  2.079442
|      8   9  0.549296  2.197225
|      9  10 -0.758542  2.302585


很方便哎，
>>> a
    rank                   country  area_sqkm  population_2013

#要抽那一個欄位，只要打a.country or a.area_sqkm

由這可以知道，table中的每一個row，都是用 list去存的。
>>> a.values
array([[7, 'India', 3287590, 1252139596, 380.86853774345343],
           [35, 'Pakistan', 803940, 182142594, 226.56242256884843],
                  [32, 'Nigeria', 923768, 173615345, 187.9425840687272],

"""

