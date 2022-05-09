#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        i = 1
        j = 0
        plat = 1
        while (i < len(arr)):
            if arr[i] > dep[j]:
                i+=1
                j+=1
            else:
                plat+=1
                i+=1
        return plat
        
        
        # times = []
        # for i in range(n):
        #     times.append([arr[i],dep[i]])
        
        # result = [[times[-1]]]
        
        # for j in range(-2, -len(times)-1, -1):
        #     if times[j][0] > result[-1][1]:
        #         result[-1].append([times])
        #     elif times[j][0] < result[-1][1]:
        #         result.append(times[j][0])
                
            
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends