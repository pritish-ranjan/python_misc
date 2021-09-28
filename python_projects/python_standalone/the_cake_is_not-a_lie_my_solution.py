def solution(s):
    if not s.isalpha() or not bool(s):
        return 0
    length_s = len(s)
    output = 0

    if(length_s <= 199): 
        i = length_s
        while i > 0:
            substr_counter = int(length_s / i)
            if (substr_counter * i) == length_s:
                valid = 1
                substr_s = s[:substr_counter]
                j = 1
                while j < i:
                    if not s[j*substr_counter:j*substr_counter+substr_counter] == substr_s:
                        valid = 0
                        break
                    j = j + 1
            if bool(valid):
                output = i
                break
            i -= 1
    return output

print(solution("1111"))