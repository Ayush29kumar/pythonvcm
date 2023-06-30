with open("a.csv" , "r") as f:
    z = []
    for i in f.readlines():
        i = i.lower()
        z.append(i.strip())
with open("a.csv" , "w") as f:
     for i in z:
        f.write(i+"\n")

