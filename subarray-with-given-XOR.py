class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        # Bruteforce
        # count = 0
        # for i in range(len(A)):
        #     xor_result = 0
        #     for j in range(i, len(A)):
        #         xor_result = xor_result ^ A[j]
        #         if xor_result == B:
        #             count += 1
        # return count   

        hash_map = {}
        count = 0
        xor_result = 0
        for i in range(len(A)):
            xor_result ^= A[i]
            if xor_result ^ B in hash_map.keys():
                count += hash_map[xor_result ^ B]
            if xor_result == B:
                count += 1

            if xor_result  in hash_map.keys():
                hash_map[xor_result] += 1
            else:
                hash_map[xor_result] = 1

        return count
