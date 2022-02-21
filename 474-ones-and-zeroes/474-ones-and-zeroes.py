class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0,0,0)}
        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros
            part_dp = set()
            for z, o ,v in dp:
                if zeros + z <= m and ones + o <= n:
                    part_dp.add((zeros + z, ones + o ,v + 1))
            dp |= part_dp
        return max(v for _, _, v in dp)

 # Usage of |=   
#     >>> s1 = {"a", "b", "c"}
#     >>> s2 = {"d", "e", "f"}

#     >>> # OR, | 
#     >>> s1 | s2
#     {'a', 'b', 'c', 'd', 'e', 'f'}
#     >>> s1                                                     # `s1` is unchanged
#     {'a', 'b', 'c'}

    ## In-place OR, |=
    # >>> s1 |= s2
    # >>> s1                                                     # `s1` is reassigned
    # {'a', 'b', 'c', 'd', 'e', 'f'}