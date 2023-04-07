a=[]
def counting(arg,s=""):
    v=len(a)
    for i in range(len(arg)):
        count=0
        if arg[i]!=s:
            for j in range(i,len(arg)):
                if arg[i]==arg[j]:
                    s=arg[i]
                    count+=1
                else:
                    break
        if count!=0:
            a.extend([arg[i],count])
    return a[v:]           
b=[1]
for i in range(6):
    print(b)
    b=counting(b)
    