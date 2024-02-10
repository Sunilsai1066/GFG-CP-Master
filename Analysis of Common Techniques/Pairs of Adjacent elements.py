#User function Template for python3

class Solution:
    def adjacentPairs(self, N, arr):
        Ind_1, Ind_2, Counter = 0, 1, 0
        for i in range(N-1):
            if(Ind_2 < N and arr[Ind_1]+1 == arr[Ind_2]):
                Counter += 1
            Ind_1, Ind_2 = Ind_2, Ind_2 + 1

        return Counter



#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.adjacentPairs(N, arr))
# } Driver Code Ends
