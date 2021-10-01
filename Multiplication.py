row=[]
column=["",1,2,3,4,5,6,7,8,9,]
i=1
print(column)
while i<10:
    for m in range(10):
        prod=m*i
        if prod==0:
            prod=i
        row.append(prod)
    print(row)
    row=[]
    i+=1
