l=list(map(int,input().split()))
d,l2={},[]
for i in l:
  d[i]=l.count(i)
print(d)
m=max(d.values())
for i in range(1,m+1):
  l1=[]
  for j in d:
    if d[j]==i:
      l1.append(j)
  l1.sort()
  for i in l1:
    l2.append(i)
print(l2)
    
      