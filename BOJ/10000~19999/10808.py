import string

a = input()
alpha_list = string.ascii_lowercase
count_list = ['0'] * len(alpha_list)
for i in a:
    for j in range(len(alpha_list)):
        if i == alpha_list[j]:
            count_list[j] = str(a.count(alpha_list[j]))

print(' '.join(count_list))
