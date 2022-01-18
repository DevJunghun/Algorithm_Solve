import sys

n = int(sys.stdin.readline())
word_list = [ sys.stdin.readline().rstrip() for _ in range(n) ]
num_dict = {}

for i in range(len(word_list)):
  for j in range(len(word_list[i])):
    if word_list[i][j] not in num_dict:
      num_dict[word_list[i][j]] = pow(10, len(word_list[i]) - j - 1)
    else:
      num_dict[word_list[i][j]] += pow(10, len(word_list[i]) - j - 1)

result_list = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
result, n = 0, 9

for i in result_list:
  result += n * i[1]
  n -= 1
print(result)