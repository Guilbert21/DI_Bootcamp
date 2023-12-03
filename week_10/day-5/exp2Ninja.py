num_set = set([6, 4, 100, 5, 200, 2, 3])
longest_len = 0

for num in num_set:
    if num - 1 not in num_set:
        cur_len = 1
        cur_num = num
        
        while cur_num + 1 in num_set:
            cur_len += 1
            cur_num += 1
        
        longest_len = max(longest_len, cur_len)

print(longest_len)

