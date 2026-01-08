class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        dp = [[-10**18 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                product = nums1[i]* nums2[j]

                dp[i][j] = product

                if i>0 and j>0:
                    dp[i][j] = max(dp[i][j], product + dp[i-1][j-1])
                
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] )

                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1] )
                
        return dp[n-1][m-1]

