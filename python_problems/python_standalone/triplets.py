# // Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# // Such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# // Notice that the solution set must not contain duplicate triplets.
# // Input: nums = [-1,0,1,2,-1,-4]
# // Output: [[-1,-1,2],[-1,0,1]]

def solution(list_A):
    list_A.sort()
    array = []
    for i in range(0, len(list_A)):
        for j in range(i+1, len(list_A)):
            for k in range(j+1, len(list_A)):
                if list_A[i] + list_A[j] + list_A[k] == 0:
                    array.append([list_A[i], list_A[j], list_A[k]])
                   
    final = [list(t) for t in set(tuple(arr) for arr in array)]
    print(type(final))
    print(final)

solution([-1,0,1,2,-1,-4,-2,-3,3,0,4])

