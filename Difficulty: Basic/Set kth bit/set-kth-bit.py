#User function Template for python3
class Solution:
	def setKthBit(self, n, k):
		# code here
		x=1<<k
		return n|x

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, K = input().split()
        N = int(N)
        K = int(K)
        ob = Solution()
        ans = ob.setKthBit(N, K)
        print(ans)

# } Driver Code Ends