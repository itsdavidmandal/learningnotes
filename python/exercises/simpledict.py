

diction = {"apple":"fruit", "banana": "fruit" , "tomato":"vegetable" , "potato":"vegetable"}
inp = str(input("What u want to search ?"))
intmod = inp.lower()

if intmod in diction :
    print(diction.get(intmod))
    
else:
    print ("try again")

