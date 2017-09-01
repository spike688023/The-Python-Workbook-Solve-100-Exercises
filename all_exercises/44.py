#FromScratch - Create a script that generates a file where all letters of English alphabet are listed three in each line

import string

letters = string.ascii_lowercase + " "

slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[2::3]

with open("letters.txt", "w") as file:
    for s1, s2, s3 in zip(slice1, slice2, slice3):
        print(s1, s2, s3)
        file.write(s1 + s2 + s3 + "\n")


"""
pen("letters3.txt","w")

print("size of string.ascii_lowercase is "+str(len(string.ascii_lowercase)))

for i in range(0,len(string.ascii_lowercase),3):
    print(string.ascii_lowercase[i:i+3])
    file.write(string.ascii_lowercase[i:i+3]+"\n")

file.close()

"""
