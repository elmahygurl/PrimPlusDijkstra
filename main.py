import heapq  #provides heap-based priority queues

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]   #list to store the graph's edges

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def prim_mst(self,source):
        visited = [False] * self.num_vertices   #to keep track of visited vertices
        min_heap = []   #to store edges with their weights
        mst_cost = 0
        parent = [-1] * self.num_vertices  # to keep track of parent vertices
        heapq.heappush(min_heap, (0, source))  #start at vertex 0 and add it to the heap with a weight of 0
        # heappush O(log n), n is the number of elements in the heap
        while min_heap: #while heap isn't empty
            weight, vertex = heapq.heappop(min_heap)  #extract min vertex  (vlogE)
            if visited[vertex]: #ignore if visited
                continue

            visited[vertex] = True
            mst_cost += weight
            for neighbor, edge_weight in self.adj_list[vertex]:    #adjacent verticies
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
                    parent[neighbor] = vertex
        print("MST Cost:", mst_cost)
        print("MST Path:")
        for i in range(self.num_vertices):
            if i != source:
                path = []
                j = i
                while j != -1:
                    path.append(j)
                    j = parent[j]
                print(f"Vertex {i}: {' -> '.join(map(str, path[::-1]))}")

    def dijkstra(self, source):
        dist = [9999999] * self.num_vertices   #assuming infinity distance
        dist[source] = 0  #as we moved 0 distance
        min_heap = []    #priority queue
        heapq.heappush(min_heap, (0, source))

        while min_heap:
            distance, vertex = heapq.heappop(min_heap)    #extract min vertex  (vlogE)

            if distance > dist[vertex]:   #ignoring
                continue

            for neighbor, edge_weight in self.adj_list[vertex]:
                new_distance = distance + edge_weight

                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbor))   #updating the priority queue

        return dist

    def short_dijkstra(self,source):
        dist = self.dijkstra(source)
        print("Shortest Paths from vertex ",source,":")
        for i in range(self.num_vertices):
            if i != source:
                print("Vertex ",i,": ", dist[i])


g = Graph(6)  # 7 vertices

# Adding edges to the graph
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 1)
g.add_edge(0, 4, 4)
g.add_edge(1, 3, 3)
g.add_edge(1, 2, 3)
g.add_edge(1, 5, 7)
g.add_edge(3, 4, 9)
g.add_edge(3, 2, 5)
g.add_edge(2, 5, 8)

print("What do you want to do?")
choice= int(input("1.Find an MST.\n2.Find the shortest path.\n"))
source = int(input("Choose a vertex between 0 and 5 as your starting vertex: "))
while source<0 or source>6:

    print("Invalid input")
    source = int(input("Choose a vertex between 0 and 6 as your starting vertex: "))
if choice==1:
    g.prim_mst(source)
elif choice==2:
    g.short_dijkstra(source)



