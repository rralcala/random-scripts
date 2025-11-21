from typing import List
import unittest


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mtx = []
        for i in range(len(points)):
            mtx.append([])
            for j in range(len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                mtx[i].append(dist)
        self.V = len(points)
        self.graph = mtx
        return self.primMST()

    def minKey(self, key, mstSet):
        min = 4000001

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self) -> int:
        # Key values used to pick minimum weight edge in cut
        key = [4000001] * self.V
        parent = [0] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for _ in range(self.V):
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if (
                    self.graph[u][v] > 0
                    and mstSet[v] == False
                    and key[v] > self.graph[u][v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        s = 0
        for i in range(1, self.V):
            s = s + self.graph[i][parent[i]]
        return s


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(
            Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]),
            20,
        )
        self.assertEqual(Solution().minCostConnectPoints([[0, 0]]), 0)


unittest.main()
