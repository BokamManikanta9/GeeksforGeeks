#User function Template for python3

class Solution:
    def half(self, N):
        # code here
        if N==1:
            return 1
        return N>>1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.half(N))
        print("~")
# } Driver Code Ends