'''
https://leetcode.com/problems/pascals-triangle/description/
'''
class Solution:
    keystore = {}
    @staticmethod
    def getSum(a: int, b: int) -> int:
        if (a, b) in Solution.keystore.keys():
            return Solution.keystore[(a, b)]
        elif (b, a) in Solution.keystore.keys():
            return Solution.keystore[(b, a)]
        else:
            c = a + b
            Solution.keystore[(a, b)] = c
            Solution.keystore[(b, a)] = c
            return c

    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1], [1, 1]]
        if numRows == 1:
            return triangle[:1]
        elif numRows == 2:
            return triangle
        else:
            for i in range(3, numRows + 1):
                row = [1]
                lastrow = triangle[(i-1)-1]
                for j in range((i-1)-1):
                    row.append(Solution.getSum(lastrow[j], lastrow[j+1]))
                row.append(1)
                triangle.append(row)
            return triangle

print(Solution().generate(5))