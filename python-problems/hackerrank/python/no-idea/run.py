n, m = (int(i) for i in input().split())
array = map(int, input().strip().split(' '))
set_a = set(map(int, input().strip().split(' ')))
set_b = set(map(int, input().strip().split(' ')))
happyness = 0
for i in array:
    if i in set_a:
        happyness += 1
    elif i in set_b:
        happyness -= 1
print(happyness)