from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
count_list = [-1] * len(alphabet_list)
slist = input()

for i in range(len(slist)):
    count_list[alphabet_list.index(slist[i])] = slist.find(slist[i])

for i in range(len(count_list)):
    count_list[i] = str(count_list[i])
print(' '.join(count_list))