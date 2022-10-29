import re
import sys

t = int(sys.stdin.readline())
test_list = [ sys.stdin.readline().replace('\n', '') for _ in range(t) ]

pattern = re.compile(r'(100+1+|01)+')
for testcase in test_list:
  if pattern.fullmatch(testcase) != None:
    print("YES")
  else:
    print("NO")