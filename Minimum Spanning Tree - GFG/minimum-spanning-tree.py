#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        active_edges=[]
        mst=[False]*V
        cost=0
        heapq.heappush(active_edges,[0,1])

        while len(active_edges)!=0:
            wt,node=heapq.heappop(active_edges)
    
            if mst[node]:
                continue

            mst[node]=True
            cost+=wt
    
            for v,w in adj[node]:
    
                if not mst[v]:
                    heapq.heappush(active_edges,[w,v])
        return cost

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends