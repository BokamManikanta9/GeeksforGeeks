#User function Template for python3
import math
class Solution:
    def isBitSet (self, N):
        # code here 
        if N==0:
            return 0
        z=int(math.log2(N)+1)
        for i in range(z):
            if N&1<<i==0:
                return 0
            else:
                continue
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isBitSet(N))
        print("~")
# } Driver Code Ends