def merge_the_tools(string, k):
    # your code goes here
    split = len(string) / k
    for i in range(0, len(string), k):
        string_new = string[i:i+k]
        string_sub = ''
        for s in string_new:
            if s not in string_sub:
                string_sub += s
        print(string_sub)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)