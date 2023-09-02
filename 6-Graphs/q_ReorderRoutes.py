# Reorder Routes To Make All Paths Lead To The City Zero

# TODO: I have found a solution without DFS

# n = 6  c = [[0,1], [1,3], [2,3], [4,0], [4,5]]
# n = 5  c = [[0,1], [1, 2], [3, 2], [3, 4]]

class Solution:
    def minReOrder(self, n, connections) -> int:

        # We change our list to an dictionary to speed up finding our cities.  
        # Dictionary looks for keys in O(1) but if we try to find something in Lists, it takes O(N)
        edges = set()
        for a,b in connections:
            edges.add((a,b))

        neighbours = {}

        for city in range(n):
            neighbours[city] = [] 

        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        visited = set()

        counter = 0
        print("Connections", connections)
        print("Neighbours", neighbours)
        print("Visited", visited)
        print()
        def dfs(city):

            nonlocal edges, neighbours, visited, counter

            for neighbour in neighbours[city]:
                if neighbour in visited:
                    continue
                if (neighbour, city) not in edges:
                    counter += 1
                visited.add(neighbour)
                dfs(neighbour)

        visited.add(0)
        dfs(0)

        return counter