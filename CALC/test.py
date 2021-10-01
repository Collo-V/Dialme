import math

#45*12+10-60+17*20/4 ===>20/4+45*12*17+10-60

#34+12+33/12*45
operators=["**","/","*","+","-","("]
operators1=operators.copy()

express=exp=input("Enter the expression:")

for operator in operators1:
    app=exp.count(operator)
    c=1
    while c<app:
        operators.append(operator)
        c=c+1
ops=[p for p in exp]
ops=[op for op in ops if op in operators]


for operator in operators:
    nums=exp.replace(operator,",")
    exp=nums
nums=nums.split(",")
#nums.pop()
nums=[float(num) for num in nums ]
print(f"Nums{nums}")
print(f"OPS:{ops}")

expr=[]
for a in range(len(nums)):
    expr.append(nums[a])
    try:expr.append(ops[a])
    except:pass
print(expr)

print(f"operators:{operators}")
res=[]
for operator in operators:
    if operator in expr:
        opindx=expr.index(operator)
        num1=expr[opindx-1]
        num2=expr[opindx+1]
        if operator=="**":
            result=num1**num2
            res.extend(expr[0:opindx])
            res.append(result)
            res.extend(expr[opindx:])
        elif operator=="/":
            result=num1/num2
            res.extend(expr[0:opindx])
            res.append(result)
            res.extend(expr[opindx:])
        elif operator=="*":
            result=num1*num2
            res.extend(expr[0:opindx])
            res.append(result)
            res.extend(expr[opindx:])
        elif operator=="+":
            result=num1+num2
            res.extend(expr[0:opindx])
            res.append(result)
            res.extend(expr[opindx:])
        elif operator=="-":
            result=num1-num2
            res.extend(expr[0:opindx])
            res.append(result)
            res.extend(expr[opindx:])
            expr.remove(expr[opindx])
        elif operator=="...":
            result=num1/num2
            res.extend(expr[0:opindx])
            res.append(result)
            res.extend(expr[opindx:])
        
        expr=res.copy()
        print(res)






