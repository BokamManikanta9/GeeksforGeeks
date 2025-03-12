#User function Template for python3


class Solution:
    def findMissing(self, arr1,arr2):
        # code here
        xor=0
        arr=arr1+arr2
        for i in arr:
            xor=xor^i
        return xor



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        l = ob.findMissing(arr1, arr2)
        print(l)
        print("~")

# } Driver Code Ends