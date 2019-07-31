from itertools import combinations
y,z=map(int,input().split())
x=len(str(y))
lst=list(combinations(str(y),x-z))
lst=sorted(lst)
print(*lst[0],sep='')
