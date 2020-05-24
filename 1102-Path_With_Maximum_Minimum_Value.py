class Solution(object):
    def maximumMinimumPath(self,A):
        res = float('inf')
        m,n = len(A),len(A[0])
        minHeap = [(-A[0][0],0,0)]
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        while minHeap:
            print(minHeap)
            val,i,j = heapq.heappop(minHeap)
            # print(val,i,j,A[i][j])
            
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if A[i][j] < res:
                res = A[i][j]
            if i == m-1 and j == n-1:
                return res
            for dx,dy in direction:
                x,y = i+dx,j+dy
                if 0<=x<m and 0<=y<n and (x,y) not in visited:
                    heapq.heappush(minHeap,(-A[x][y],x,y))
        return res
