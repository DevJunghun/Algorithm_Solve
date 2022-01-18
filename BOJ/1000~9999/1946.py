import sys

test_case = int(sys.stdin.readline())
for i in range(test_case):
  n = int(sys.stdin.readline())
  applicant_list = sorted([ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ], key=lambda x:x[0])
  rank = applicant_list[0][1]
  cnt = 1

  for j in range(1, len(applicant_list)):
    if rank > applicant_list[j][1]:
      rank = applicant_list[j][1]
      cnt += 1
  print(cnt)