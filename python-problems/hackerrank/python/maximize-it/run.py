# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

if __name__ == '__main__':
    k, n = map(int, input().strip().split(' '))
    s_max = 0
    list_max = None
    list_temp = list()
    for i in range(k):
        l = list(map(int, input().strip().split(' ')))
        list_temp.append(l[1:])
    # Loop through Cartesian product of list to get S_max
    for l in itertools.product(*list_temp):
        s = sum([x**2 for x in l]) % n
        if s > s_max:
            s_max = s
            list_max = l
    print(s_max)