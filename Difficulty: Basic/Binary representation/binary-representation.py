#User function Template for python3
import math
class Solution:
	def getBinaryRep(self, n):
		# code here
		s=""
		for i in range(30):
		    if n&1<<i:
		        s='1'+s
		    else:
		        s='0'+s
		return s
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.getBinaryRep(n)
		print(ans)

# } Driver Code Ends