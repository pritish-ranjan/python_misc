def solution(s):
    length_s = len(s)

    if len(set(s)) == 1:
        return length_s

    if length_s > 1:
        or_factors = sorted(get_len_factors(length_s))
        print(or_factors)
        return get_s_min_chunk(or_factors, s, length_s)

    return 1


def get_len_factors(len_s):
    factor_list = []
    upper_limit = int(len_s ** 0.5 + 1)
    print(upper_limit)

    for i in range(2, upper_limit):
        if len_s % i == 0:
            factor_list.extend([i, int(len_s / i)])
            print("factor_list", factor_list)

    return set(factor_list)


def get_s_min_chunk(or_factors, s, len_s):
    for i in or_factors:
        if s[:i] == s[-i:]:
            num_sub_s = s.count(s[:i])
            if num_sub_s * i == len_s:
                return int(len_s / i)
    return 1

print(solution('aaaaaaaabb'))