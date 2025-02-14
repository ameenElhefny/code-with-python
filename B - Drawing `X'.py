n=int(input())
k=(n+1)/2
s=""
for i in range (1,n+1):
    for j in range(1, n + 1):
        if(i==j) and not i==j==k:
            s+="\\"
        elif i== k== j:
            s+="X"
        elif (i !=j) and i+j==n+1:
            s+="/"
        else :
            s+="*"
    if(i!=n+1):
        s+="\n"
print(s)

