'''

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 =