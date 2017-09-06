"""
我看演示,  會一直加上去, 所以, 我用a 
"""

userinput = input("Enter values:")
list1 = userinput.split(",")
file = open("95_writting.txt","a+")
print(list1)
for i in list1:
    file.write(i+"\n")
file.close()
