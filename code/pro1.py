m=int(input())
p=[]
for i in range(0,m):
  t1=input()
  p.append(t1)
s=[]
for i in zip(*p):
  if(i.count(i[0])==len(i)):
    s.append(i[0])
  else:
    break
print(''.join(s))
