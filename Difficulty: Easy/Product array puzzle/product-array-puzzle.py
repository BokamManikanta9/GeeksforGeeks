#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        l=[1]*n
        left=1
        right=1
        for i in range(n):
            l[i]=left
            left*=nums[i]
        for i in range(n-1,-1,-1):
            l[i]*=right
            right*=nums[i]
        return l
                
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends