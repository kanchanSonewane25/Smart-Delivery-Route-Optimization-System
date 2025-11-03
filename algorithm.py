import itertools

# ---------- Disjoint Set (for Kruskal) ----------
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False


# ---------- Kruskal’s Algorithm ----------
def kruskal(nodes, edges):
    sorted_edges = sorted(edges, key=lambda e: e[2])
    ds = DisjointSet(nodes)
    mst_edges = []
    total_cost = 0

    for u, v, w in sorted_edges:
        if ds.union(u, v):
            mst_edges.append((u, v, w))
            total_cost += w

    return mst_edges, total_cost


# ---------- Bellman-Ford Algorithm ----------
def bellman_ford(nodes, edges, source):
    distances = {n: float('inf') for n in nodes}
    predecessors = {n: None for n in nodes}
    distances[source] = 0

    all_edges = []
    for u, v, w in edges:
        all_edges.append((u, v, w))
        all_edges.append((v, u, w))

    for _ in range(len(nodes) - 1):
        for u, v, w in all_edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                predecessors[v] = u

    # Detect negative cycle
    for u, v, w in all_edges:
        if distances[u] + w < distances[v]:
            return None, None

    return distances, predecessors


# ---------- Travelling Salesman Problem (Brute Force) ----------
def tsp_brute_force(cost_matrix, start_node, destinations):
    min_cost = float('inf')
    best_path = []

    for perm in itertools.permutations(destinations):
        path = [start_node] + list(perm) + [start_node]
        cost = 0
        valid = True

        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            step_cost = cost_matrix[u][v]
            if step_cost == float('inf') or step_cost == 999:
                valid = False
                break
            cost += step_cost

        if valid and cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost
