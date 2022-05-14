#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        queue = [0]
        visited = {}
        visited[0] = True
        arr = []
        while queue :
            s = queue.pop(0)
            
            arr.append(s)
            for nbr in adj[s]:
                if nbr not in visited:
                    visited[nbr] = True
                    queue.append(nbr)
                    
        return arr            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
           
        # queue = [0]
        # arr = []
        # visited = {0:True}
        # while(queue):
        #     s = queue.pop(0)
        #     arr.append(s)
        #     for neighbor in adj[s]:
        #         if neighbor not in visited:
        #             visited[neighbor] = True
        #             queue.append(neighbor)
                
        # return arr            
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends