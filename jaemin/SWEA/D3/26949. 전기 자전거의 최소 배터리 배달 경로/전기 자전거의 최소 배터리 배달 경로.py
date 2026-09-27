import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]

    # (현재까지 배터리 소비량, 행, 열)
    pq = [(0, 0, 0)]
    dist[0][0] = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while pq:
        cost, r, c = heapq.heappop(pq)

        # 이미 더 적은 비용으로 방문한 적이 있다면 무시
        if cost > dist[r][c]:
            continue

        # 목적지에 도착
        if r == N - 1 and c == N - 1:
            break

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:

                # 기본 이동 비용 1
                move_cost = 1

                # 올라가는 경우 높이 차이만큼 추가
                if graph[nr][nc] > graph[r][c]:
                    move_cost += graph[nr][nc] - graph[r][c]

                new_cost = cost + move_cost

                # 더 적은 비용으로 갈 수 있다면 갱신
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

    print(f"#{tc} {dist[N - 1][N - 1]}")