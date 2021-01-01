#!/usr/bin/env python3

def count_pairs(month_number, offspring_number):
    if month_number == 1:
        return 1
    elif month_number == 2:
        return offspring_number
    gen_one = count_pairs(month_number - 1, offspring_number)
    gen_two = count_pairs(month_number - 2, offspring_number)
    if month_number <= 4:
        return gen_one + gen_two
    return gen_one + (gen_two * offspring_number)

def main():
    print('How many month?')
    m = int(input('Month = '))
    print('How many offsprings each pair has?')
    k = int(input('Offsprings = '))
    print(count_pairs(m, k))

if __name__ == "__main__":
    main()