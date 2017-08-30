#Create a script that converts all items of the range to strings
my_range = range(1, 21)
print(map(str, my_range))


# 這裡因為 map object不能直接取用,所以, 我用iter
print("Rewrite")
for i in iter(map(str, my_range)):
    print(type(i))
    print(i)


print("Rewrite2")
print([ x for x in iter(map(str, my_range)) ])



# I wrote
print("spike")
print([ str(x) for x in my_range ])
