import sys

k, s, n = map(str, sys.stdin.readline().split())
n = int(n)
move_list = [ sys.stdin.readline().replace('\n', '') for _ in range(n) ]
direction = { 'R':(1, 0), 'L':(-1, 0), 'B':(0, -1), 'T':(0, 1), 'RT':(1, 1), 'LT':(-1, 1), 'RB':(1, -1), 'LB':(-1, -1) }

cur_k = (int(ord(k[0]) - 64), int(k[1]))
cur_s = (int(ord(s[0]) - 64), int(s[1]))

for move in move_list:
  k_x = cur_k[0] + direction[move][0]
  k_y = cur_k[1] + direction[move][1]
  s_x = cur_s[0] + direction[move][0]
  s_y = cur_s[1] + direction[move][1]

  if (1 <= k_x <= 8) and (1 <= k_y <= 8):
    if (k_x, k_y) == cur_s:
      if (1 <= s_x <= 8) and (1 <= s_y <= 8):
        cur_s = (cur_s[0] + direction[move][0], cur_s[1] + direction[move][1])
        cur_k = (cur_k[0] + direction[move][0], cur_k[1] + direction[move][1])

    else:
      cur_k = (cur_k[0] + direction[move][0], cur_k[1] + direction[move][1])

cur_k = (chr(cur_k[0] + 64), cur_k[1])
cur_s = (chr(cur_s[0] + 64), cur_s[1])

print(f"{cur_k[0]}{str(cur_k[1])}\n{cur_s[0]}{str(cur_s[1])}")