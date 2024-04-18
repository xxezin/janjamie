n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = []

def func(start):
    if len(ans)==m:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(start,n):
        if A[i] not in ans:
            ans.append(A[i])
            func(i+1)
            ans.pop()

func(0)
