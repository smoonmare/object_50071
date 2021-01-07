def minion_game(string):
    # your code goes here
    vovels = 'AEIOU'
    length_string = len(string)
    score_kevin = 0
    score_stuart = 0
    for i in range(length_string):
        if s[i] in vovels:
            score_kevin += (length_string - i)
        else:
            score_stuart += (length_string - i)
    if score_kevin > score_stuart:
        print('Kevin', score_kevin)
    elif score_stuart > score_kevin:
        print('Stuart', score_stuart)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)