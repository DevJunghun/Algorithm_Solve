n = sorted(list(input()), reverse=True)
print(-1) if sum(map(int, n)) % 3 != 0 or '0' not in n else print("".join(n)) 
