with open("a.txt" , "r") as f:
    z=""
    k={}
    x=[]
    a = "normal sentence"
    for i in f.readlines():
        i = i.replace("." , "")
        x.append(f"{i.strip()},{a}")
        #z += f"'{i.strip()}' : {a},"
        #z += "'"+i.strip()+"'"+ a +","

    print(z)
with open("a.txt" , "w") as f:
    for j in x:
        f.write(j+"\n")
    f.write(z)


