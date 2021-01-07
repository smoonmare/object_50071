import re

regex_integer_in_range = r'^[1-9][\d]{5}$'	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'	# Do not delete 'r'.
P = input()
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
'''
Explenation:
  ^[1-9][\d]{5}$ / gm
    -  ^ asserts position at start of a line
    -  Match a single character present in the list below [1-9]
        1-9 a single character in the range between 1 (index 49) and 9 (index 57) (case sensitive)
    -  Match a single character present in the list below [\d]{5}
        {5} Quantifier — Matches exactly 5 times
    -  \d matches a digit (equal to [0-9])
        $ asserts position at the end of a line
    -  Global pattern flags
        g modifier: global. All matches (don't return after first match)
        m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
  (\d)(?=\d\1) / gm
    -  1st Capturing Group (\d)
        \d matches a digit (equal to [0-9])
    -  Positive Lookahead (?=\d\1)
        Assert that the Regex below matches
        \d matches a digit (equal to [0-9])
        \1 matches the same text as most recently matched by the 1st capturing group
    -  Global pattern flags
        g modifier: global. All matches (don't return after first match)
        m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
'''