# Given [3,5,3,3,6,5] - 4
#        0 1 2 3 4 5 6 
# Find how many indices(pair of indexes) are formed with the repeating numbers

# Brute force O(n^2)

# def solution(A):

#     length_A = len(A)
#     count = 0
#     for i in range(0, length_A): # 5
#         for j in range(i+1, length_A): #  3
#             if (A[i]==A[j]):
#                 count +=1 # 4
#     return count

# print(solution([3,1,2,4]))

# Smarter solution O(n)

def solution(A):
    
    dict = {}

    for i in range(0, len(A)):
        # print (A[i])
        # if A[i] == A[i+1]:
        if A.count(A[i]) > 1:
            dict[A[i]] = A.count(A[i])
            # dict[A[i]] = i
    return dict

print(solution([3,1,2,3,4,3,7,3]))

# import java.util.ArrayList;
# import java.util.HashMap;

# public class FindIndices {
#     ArrayList<Integer> index;
#     int totalPair=0;
#     public static void main(String args[])  //static method
#     {
#         System.out.println("Static method");
#         int[] arr={3,5,3,3,6,5};
#         FindIndices fi=new FindIndices();
#         int indicesPair = fi.indicesPair(arr);
#         System.out.println(indicesPair);
#     }

#     int indicesPair(int[] arr){
#         HashMap<Integer, ArrayList<Integer>> map=new HashMap<Integer, ArrayList<Integer>>();
#         for(int i=0;i<arr.length; i++){
#             if(!map.containsKey(arr[i])){
#                 index=new ArrayList<>();
#                 index.add(i);
#                 map.put(arr[i],index);
#             }else{
#                 index=map.get(arr[i]);
#                 for(int j=0;j<index.size();j++){
#                     System.out.println(index.get(j)+","+i);
#                     totalPair+=1;
#                 }
#                 index.add(i);
#                 map.put(arr[i],index);
#             }
#         }
#         for(int i:map.keySet()){
#             System.out.println(i+" ,"+map.get(i));
#         }
#         return totalPair;
#     }
# }


