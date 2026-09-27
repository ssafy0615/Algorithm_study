T = 10

for tc in range(1, T + 1):
    input()
    target = input()
    text = input()

    count = 0
    target_len = len(target)

    for i in range(len(text) - target_len + 1):
        if text[i:i + target_len] == target:
            count += 1

    print(f"#{tc} {count}")