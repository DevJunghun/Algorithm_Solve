number = int(input())
word_list = [ input() for i in range(number) ]
sorted_word_set = sorted(set(word_list), key = lambda x: (len(x), x))

for i in sorted_word_set:
    print(i)