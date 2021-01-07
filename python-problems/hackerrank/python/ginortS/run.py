def sort_string(string):
    case_lower = []
    case_upper = []
    digit_even = []
    digit_odd = []
    for s in string:
        if s.islower():
            case_lower.append(s)
        elif s.isupper():
            case_upper.append(s)
        elif s.isdigit():
            if int(s) % 2 == 0:
                digit_even.append(s)
            else:
                digit_odd.append(s)
    return (''.join(sorted(case_lower)+sorted(case_upper)+sorted(digit_odd)+sorted(digit_even)))

if __name__ == '__main__':
    string_input = input()
    print(sort_string(string_input))