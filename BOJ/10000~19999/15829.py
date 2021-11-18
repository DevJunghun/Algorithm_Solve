import string

a = string.ascii_lowercase
hash_dic = {}
for i in range(1, len(a) + 1):
    hash_dic[a[i - 1]] = i

num = int(input())
alpha = input()
res = 0

for i in range(num):
    res += int(hash_dic[alpha[i]]) * pow(31, i)

print(res % 1234567891)