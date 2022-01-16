
class Digits:
    
    def solution(self, N):

        result = self.create_result_set(N)
        print(result)

    def create_result_set(self, N):
        absolute_N = abs(N)
        list_N = [int(digit) for digit in str(absolute_N)]
        print(list_N)
        
        array = []
        if 5 in list_N:
            for i in range(0, len(list_N)):
                new_list = list_N.copy()
                if list_N[i] == 5:
                    new_list.pop(i)
                    s = ''.join(map(str, new_list))
                    print(type(s))
                    candidate = int(s)
                    array.append(candidate)
            if N < 0:
                return -abs(min(array))
            return max(array)
        return N

obj = Digits()
obj.solution(15958)