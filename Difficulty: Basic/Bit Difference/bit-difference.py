#User function Template for python3
import math
class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self, a, b):
        c=0
        ##Your code here
        x=a^b
        if x==0:
            return 0
        z=int(math.log2(x)+1)
        for i in range(z):
            if x&1<<i:
                c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        ab = [int(x) for x in input().strip().split()]
        a = ab[0]
        b = ab[1]
        ob = Solution()
        print(ob.countBitsFlip(a, b))
        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends