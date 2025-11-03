from algorithm import kruskal, bellman_ford, tsp_brute_force
import graph_data
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("\n===== SMART DELIVERY ROUTE OPTIMIZATION =====")

    # ---------------- Kruskal’s Algorithm ----------------
    print("\n=== Kruskal’s Algorithm (Minimum Spanning Tree) ===")
    mst, total_cost = kruskal(graph_data.GRAPH_NODES.keys(), graph_data.GRAPH_EDGES)
    for u, v, w in mst:
        print(f"  {u} <-> {v}  (Cost: {w})")
    print(f" Total MST Cost: {total_cost}")

    # ---------------- Bellman-Ford Algorithm ----------------
    print(f"\n=== Bellman-Ford Algorithm (Source: {graph_data.WAREHOUSE}) ===")
    dist, pred = bellman_ford(
        graph_data.GRAPH_NODES.keys(),
        graph_data.GRAPH_EDGES,
        graph_data.WAREHOUSE
    )

    if dist is None:
        print("Error: Negative-weight cycle detected!")
    else:
        for node, d in dist.items():
            if node == graph_data.WAREHOUSE:
                continue
            path = []
            curr = node
            while curr:
                path.insert(0, curr)
                curr = pred[curr]
            print(f"  To {node}: Cost {d}, Path: {' -> '.join(path)}")

    # ----------------Travelling Salesman Problem ----------------
    print("\n=== Travelling Salesman Problem (Brute Force) ===")
    destinations = [n for n in graph_data.GRAPH_NODES.keys() if n != graph_data.WAREHOUSE]
    path, cost = tsp_brute_force(graph_data.TSP_MATRIX, graph_data.WAREHOUSE, destinations)
    print(f"Optimal Path: {' -> '.join(path)}")
    print(f"Total Travel Cost: {cost}")

    # ---------------- Plot Only TSP Route ----------------
    print("\nPlotting the Optimal TSP Route...")

    G_tsp = nx.Graph()
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        G_tsp.add_edge(u, v, weight=graph_data.TSP_MATRIX[u][v])

    pos = graph_data.GRAPH_NODES
    plt.figure(figsize=(6, 5))
    nx.draw(
        G_tsp,
        pos=pos,
        with_labels=True,
        node_color="#3498db",
        node_size=1000,
        font_weight="bold"
    )
    nx.draw_networkx_edge_labels(G_tsp, pos, edge_labels=nx.get_edge_attributes(G_tsp, "weight"))
    plt.title("Travelling Salesman Optimal Route", fontsize=14)
    plt.show()

    print("\nAll algorithms executed successfully!")
