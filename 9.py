a=[ ["1","4","7"],"a",["b",["t",["9","1",["u",["8"],"1"],"9"],"3"]],"r"]
def islist(n):
    if type(n)==list:
        return True
    else:
        return False
b=0
n=0
def f(d):
    global b
    global n
    for i in d:
        if islist(i):
            b+=1
            return f(i)
    n+=1
    b=0
    return f(a[n:])
f(a)
print(b)
