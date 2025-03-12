#User function Template for python3
import math
class Solution:
	def setBit(self, n):
		# code here
		if n==0:
		    return 1
		z=int(math.log2(n)+1)
		for i in range(z):
		    if n&1<<i == 0:
		        return n|1<<i
		return n<<1|1
	    

		

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())

        ob = Solution()
        ans = ob.setBit(N)
        print(ans)

# } Driver Code Ends