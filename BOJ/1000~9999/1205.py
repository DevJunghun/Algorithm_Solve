import sys

n, new_score, p = map(int, sys.stdin.readline().split())

if n:
  score_list = list(map(int, sys.stdin.readline().split()))
  score_list.append(new_score)
  score_list.sort(reverse=True)
  
  if p >= (score_list.index(new_score) + 1):
    if n == p and new_score <= score_list[-1]:
      print(-1)
    else:
      print(score_list.index(new_score) + 1)
  else:
    print(-1)
else:
  print(1)