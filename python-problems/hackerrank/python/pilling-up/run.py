from collections import deque

for _ in range(int(input())):
    result = True
    input()
    length_side = deque(map(int, input().strip().split()))
    if length_side[0] >= length_side[-1]:
        l_max = length_side.popleft()
    else:
        l_max = length_side.pop()
    while length_side:
        if len(length_side) == 1:
            if length_side[0] <= l_max:
                break
            else:
                result = False
                break
        else:
            if (length_side[0] <= l_max) and (length_side[-1] <= l_max):
                if length_side[0] >= length_side[-1]:
                    l_max = length_side.popleft()
                else:
                   l_max = length_side.pop()
            elif length_side[0] <= l_max:
                l_max = length_side.popleft()
            elif length_side[-1] <= l_max:
                l_max = length_side.pop()
            else:
                result = False
                break
    if result:
        print('Yes')
    else:
        print('No')