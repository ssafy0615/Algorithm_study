T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    parent = list(range(N + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            parent[b] = a

    for i in range(0, 2 * M, 2):
        a = data[i]
        b = data[i + 1]
        union(a, b)

    groups = set()

    for i in range(1, N + 1):
        groups.add(find(i))

    print(f"#{tc} {len(groups)}")