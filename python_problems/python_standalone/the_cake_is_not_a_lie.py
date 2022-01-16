def solution(s):

    if (not s.isalpha() or not bool(s) or len(s) > 199):
        return 0

    def perform_mod(inp1,inp2):
        return inp1%inp2
    def perform_integer_divison(x,y):
        return x//y
    def custom_count(element,seq):
        return element.count(seq)
    
    length_s = len(s)
    k = 1
    output = 1
    split = False
    input_cake = s
    while not split:
        k = k + 1
        if perform_mod(length_s,k) == 0:
            substr_s = input_cake[:perform_integer_divison(length_s,k)]
            repeats = custom_count(input_cake,substr_s)
            if repeats*len(substr_s) == length_s:
                output = k
            else:
                output = output
        
        if k == length_s:
            split = True
        else:
            split = False
    
    return output