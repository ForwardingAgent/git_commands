import re

lst = []
with open(r'/Users/nikolas/Desktop/Git_practice/nums.txt') as f:
    for i in f:
        nums = re.findall(r'\d+', i)
        lst.extend(nums)
sum = sum(map(int, lst))
print(sum)