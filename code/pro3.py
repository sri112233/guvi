xt,pot=input().split()
t1=abs(len(pot)-len(xt))
for m1 in range(len(xt)):
  if(len(pot)==1 and pot[m1] in xt):
    break
  if(xt[m1]!=pot[m1]):
    t1=t1+1
print(t1)
