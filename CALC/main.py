import math

#45*12+10-60+17*20/4 ===>20/4+45*12*17+10-60

#34+12+33/12*45
operators=["p","/","*","+","-","("]
operators1=operators.copy()

exp=input("Enter the expression:")


exp=exp.replace("--","+")
exp=exp.replace("+-","-")
exp =exp.replace("**","p")


for operator in operators1:
    app=exp.count(operator)
    c=1
    while c<app:
        indx=operators.index(operator)
        operators.insert(indx,operator)
        c+=1

print(operators)
ops=[p for p in exp]
ops=[op for op in ops if op in operators]


for operator in operators:
    nums=exp.replace(operator,",")
    exp=nums
nums=nums.split(",")
#nums.pop()
nums=[float(num) for num in nums ]

expr=[]
for a in range(len(nums)):
    expr.append(nums[a])
    try:expr.append(ops[a])
    except:pass
for xp in range(len(expr)):
    if expr[xp]=="-":
        expr[xp]="+"
        expr[xp+1]*=-1

#print(f"Bodmas:{expr}")
try:
    indx=operators.index("-")
    operators[indx]="+"
except:pass


#print(f"operators:{operators}")
for operator in operators:
    if operator in expr:
        opindx=expr.index(operator)
        num1=expr[opindx-1]
        num2=expr[opindx+1]
        if operator=="p":
            result=num1**num2
            expr[opindx]=result
            expr.remove(expr[opindx-1])
            expr.remove(expr[opindx])
        elif operator=="/":
            result=num1/num2
            expr[opindx]=result
            expr.remove(expr[opindx-1])
            expr.remove(expr[opindx])
        elif operator=="*":
            result=num1*num2
            expr[opindx]=result
            expr.remove(expr[opindx-1])
            expr.remove(expr[opindx])
        elif operator=="+":
            result=num1+num2
            expr[opindx]=result
            expr.remove(expr[opindx-1])
            expr.remove(expr[opindx])
        elif operator=="...":
            result=num1/num2
            expr[opindx]=result
            expr.remove(expr[opindx-1])
            expr.remove(expr[opindx])
print(f"\n{expr[0]}")






