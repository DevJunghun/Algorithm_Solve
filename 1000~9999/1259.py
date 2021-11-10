while True:
    num = input()
    if num == '0': break
    cnt = 0
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - i - 1]: cnt += 1
    print('yes') if cnt == 0 else print('no')
