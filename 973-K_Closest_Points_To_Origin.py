class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        points.sort(key = lambda point: point[0]**2 + point[1]**2)
        return points[:K]