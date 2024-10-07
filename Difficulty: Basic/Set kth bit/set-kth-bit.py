#User function Template for python3
class Solution:
	def setKthBit(self, n, K):
	    mask=1<<K
	    n=n|mask
	    return n
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,K = input().split()
		N = int(N)
		K = int(K)
		ob = Solution()
		ans = ob.setKthBit(N,K)
		print(ans)




# } Driver Code Ends