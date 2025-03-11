#User function Template for python3
import math
class Solution:
    
    #Function to check if the number is sparse or not.
    def isSparse(self,n):
        #Your code here 
        if n==0:
            return True
        z=int(math.log2(n)+1)
        for i in range(z):
            if n&1<<i and n&1<<i+1:
                return False
        return True



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isSparse(n):
            print("1")
        else:
            print("0")
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends