#User function Template for python3
class Solution:
    def onesComplement(self,S,N):
        # code here
        x=''
        for i in S:
            if i=='0':
                x+='1'
            else:
                x+='0'
        return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.onesComplement(S,N))
        print("~")
# } Driver Code Ends