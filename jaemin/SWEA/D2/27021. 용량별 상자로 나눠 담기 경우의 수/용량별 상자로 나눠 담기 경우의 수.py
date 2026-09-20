T = int(input())

for tc in range(1, T + 1):
    N, C = map(int, input().split())
    boxes = list(map(int, input().split()))

    dp = [0] * (N + 1)
    dp[0] = 1

    for box in boxes:
        for i in range(box, N + 1):
            dp[i] += dp[i - box]

    print(f"#{tc} {dp[N]}")