T = int(input())
times = 0
boms = 0
dist = []
x=[]
y=[]
t=[]
k=[]
for i in range(T):
    n, m = map(int, input().split())
    for i in range(n):
        x_i, y_i, t_i, k_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        t.append(t_i)
        k.append(k_i)

def remove_elements_by_indices(lst, indices):
    for index in sorted(indices, reverse=True):
        if 0 <= index < len(lst):
            del lst[index]
    return lst

dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist[i][j] = abs(x[i] - x[j]) + abs(y[i] - y[j])

while t:
    indices = []
    index = t.index(min(t))
    boms += 1
    indices.append(index)
    for indexj, j in enumerate(dist[index]):
        if j < k[index]:
            boms += 1
            indices.append(indexj)
    t = remove_elements_by_indices(t, indices)
    times += 1
    if n-len(t) <= m:
        break

print(times)