T = int(input())
times = 0
boms = 0
dist = []

for i in range(T):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    t = list(map(int, input().split()))
    k = list(map(int, input().split()))

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
        if not t:
            break

print(times)