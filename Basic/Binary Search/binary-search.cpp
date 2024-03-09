//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution {
  public:
  int fun(int v[],int i,int j,int k)
    {
	int m=int((i+j)/2);
		if(i>j)
		{
			return -1;
		}
	if(v[m]==k)
	{
// 		cout<<"Got it";
		return m;
	}
	else if(v[m]>k)
	{
		fun(v,i,m-1,k);
	}
	else
	{
		fun(v,m+1,j,k);
	}
    }
    int binarysearch(int arr[], int n, int k) {
        // code here
        int i=0;
    	int j=n-1;
    	return fun(arr,i,j,k);
        
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;

    while (t--) {
        int N;
        cin >> N;
        int arr[N];
        for (int i = 0; i < N; i++) cin >> arr[i];
        int key;
        cin >> key;
        Solution ob;
        int found = ob.binarysearch(arr, N, key);
        cout << found << endl;
    }
}

// } Driver Code Ends