import sys

n = int(sys.stdin.readline())
score_list = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ]
a_score = [ score_list[i][0] for i in range(len(score_list)) ]
b_score = [ score_list[i][1] for i in range(len(score_list)) ]
c_score = [ score_list[i][2] for i in range(len(score_list)) ]
sum_score = [ sum(a_score), sum(b_score), sum(c_score) ]
three_count = [ a_score.count(3), b_score.count(3), c_score.count(3) ]
two_count = [ a_score.count(2), b_score.count(2), c_score.count(2) ]

if len(sum_score) == len(set(sum_score)):
  print(f"{sum_score.index(max(sum_score)) + 1} {max(sum_score)}")
elif len(set(three_count)) == 1 and len(set(two_count)) == 1:
  print(f"0 {max(sum_score)}")
else:
  if three_count.count(max(three_count)) <= 1:
    print(f"{three_count.index(max(three_count)) + 1} {sum_score[three_count.index(max(three_count))]}")
  else:
    can_list = [ i for i in range(len(three_count)) if three_count[i] == max(three_count) ]
    two_max = []
    for i in can_list:
      two_max.append(two_count[i])
    if len(two_max) == 1:
      print(f"{two_count.index(two_max) + 1} {sum_score[two_count.index(two_max)]}")
    else:
      print(f"0 {max(sum_score)}")