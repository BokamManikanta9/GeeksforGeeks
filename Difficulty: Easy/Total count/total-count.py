#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def totalCount(self, k, arr):
        tc=0
        for i in arr:
            c=(i//k)
            if i%k!=0:
                c+=1
            tc+=c
        return tc
        # code here
        # c=0
        # for i in arr:
        #     while i-k>k:
        #         c+=1
        #         i=i-k
        #     tc=c+(i%k)
        # return tc

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.totalCount(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends