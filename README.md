# PrimPlusDijkstra
## I. Implementing Prim’s algorithm for MST
Prim's algorithm iteratively adds the edge with the minimum weight that
connects the growing MST to an unvisited vertex, ensuring that the resulting tree
is a minimum spanning tree. By following this approach, the algorithm guarantees
that the MST is gradually formed with edges of minimum weight until all vertices
are included.
The time complexity of Prim's algorithm is O (V log V + E log V), where V is the
number of vertices and E is the number of edges in the graph. The algorithm
leverages a min-heap (priority queue) data structure to efficiently select the edge
with the minimum weight in each iteration.
The space complexity of Prim's algorithm is O (V) to store the “visited” list and
“min_heap”, where V is the number of vertices in the graph.
## II. Implementing Dijkstra’s algorithm for Shortest path
The algorithm begins by initializing the distance of the source vertex as 0 and the
distance of all other vertices as infinity. It uses a priority queue, typically
implemented as a min heap, to store the vertices along with their corresponding
distances. The source vertex is inserted into the priority queue with a distance of
0.
As long as the priority queue is not empty, the algorithm continues to extract the
vertex with the minimum distance. For each neighboring vertex of the extracted
vertex, it checks if the distance can be improved by taking the current path. If a
shorter path is found, the distance of the neighboring vertex is updated, and the
neighboring vertex is inserted back into the priority queue.
The algorithm repeats this process until the priority queue becomes empty. At
that point, the distances from the source vertex to all other vertices in the graph
have been calculated. These distances represent the shortest paths from the
source vertex to each respective vertex.
