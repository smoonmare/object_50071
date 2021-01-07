import re

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        string_input = input().strip()
        match_pre = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$', string_input)
        if match_pre:
            string_processed = ''.join(match_pre.group(0).split('-'))
            match_final = re.search(r'(\d)\1{3,}', string_processed)
            if match_final:
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
'''
Explanation:
  ^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$ / gm
    -  ^ asserts position at start of a line
    -  Match a single character present in the list below [456]
        456 matches a single character in the list 456 (case sensitive)
    -  \d{3} matches a digit (equal to [0-9])
        {3} Quantifier — Matches exactly 3 times
    -  1st Capturing Group (-?)
        -? matches the character - literally (case sensitive)
        ? Quantifier — Matches between zero and one times, as many times as possible, giving back as needed (greedy)
    - \d{4} matches a digit (equal to [0-9])
        {4} Quantifier — Matches exactly 4 times
    - \1 matches the same text as most recently matched by the 1st capturing group
        \d{4} matches a digit (equal to [0-9])
        {4} Quantifier — Matches exactly 4 times
    -  \1 matches the same text as most recently matched by the 1st capturing group
        \d{4} matches a digit (equal to [0-9])
        {4} Quantifier — Matches exactly 4 times
    -  $ asserts position at the end of a line
    -  Global pattern flags
        g modifier: global. All matches (don't return after first match)
        m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
  (\d)\1{3,} / gm
    -  1st Capturing Group (\d)
        \d matches a digit (equal to [0-9])
    -  \1{3,} matches the same text as most recently matched by the 1st capturing group
        {3,} Quantifier — Matches between 3 and unlimited times, as many times as possible, giving back as needed (greedy)
    -  Global pattern flags
        g modifier: global. All matches (don't return after first match)
        m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
'''