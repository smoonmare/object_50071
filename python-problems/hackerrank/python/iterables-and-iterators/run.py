from itertools import combinations

n = int(input())
array = input().split()
k = int(input())
list_combined = list(combinations(array, k))
list_a = [i for i in list_combined if 'a' in i]
print(r'{:.3f}'.format(len(list_a) / len(list_combined)))