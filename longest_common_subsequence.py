class Solution:
    keystore = {}
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if (text1, text2) in Solution.keystore.keys():
            return Solution.keystore[(text1, text2)]
        elif (text2, text1) in Solution.keystore.keys():
            return Solution.keystore[(text2, text1)]

        max_subseq = 0
        for i, char in enumerate(text2):
            try:
                idx = text1.index(char)
                lcs = 0
                if idx != len(text1)-1 and i != len(text2)-1:
                    lcs = self.longestCommonSubsequence(text1[idx+1:], text2[i+1:])
                    Solution.keystore[(text1[idx+1:], text2[i+1:])] = lcs
                if max_subseq < lcs + 1:
                    max_subseq = lcs + 1
            except ValueError as e:
                continue
        return max_subseq

# print(Solution().longestCommonSubsequence("ambnc", "mabnc"))
print(Solution().longestCommonSubsequence("abcde", "ace"))