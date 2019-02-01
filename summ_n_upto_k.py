#shyam
x,y=map(int,input().split())
z=list(map(int,input().split()))
summ=0

for i in range(0,y):
    summ=summ+z[i]
    i=i+1
print(summ)
