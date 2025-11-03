GRAPH_NODES = {
    "A (Warehouse)": (150, 300),
    "B (Hub)": (350, 150),
    "C (Client)": (350, 450),
    "D (Hub)": (550, 300),
    "E (Client)": (750, 150),
    "F (Client)": (750, 450)
}

WAREHOUSE = "A (Warehouse)"

GRAPH_EDGES = [
    ("A (Warehouse)", "B (Hub)", 10),
    ("A (Warehouse)", "C (Client)", 15),
    ("B (Hub)", "C (Client)", 12),
    ("B (Hub)", "D (Hub)", 20),
    ("B (Hub)", "E (Client)", 30),
    ("C (Client)", "D (Hub)", 18),
    ("C (Client)", "F (Client)", 25),
    ("D (Hub)", "E (Client)", 14),
    ("D (Hub)", "F (Client)", 8),
    ("E (Client)", "F (Client)", 22)
]

def get_tsp_matrix():
    """Constructs a complete cost matrix for the TSP problem."""
    all_nodes = list(GRAPH_NODES.keys())
    full_matrix = {u: {} for u in all_nodes}

    # Default high cost for all paths
    for u in all_nodes:
        for v in all_nodes:
            full_matrix[u][v] = 0 if u == v else 999

    # Add edges
    for u, v, w in GRAPH_EDGES:
        full_matrix[u][v] = w
        full_matrix[v][u] = w

    # Add some extra 'highway' paths
    full_matrix["A (Warehouse)"]["E (Client)"] = full_matrix["E (Client)"]["A (Warehouse)"] = 45
    full_matrix["A (Warehouse)"]["F (Client)"] = full_matrix["F (Client)"]["A (Warehouse)"] = 40
    full_matrix["B (Hub)"]["F (Client)"] = full_matrix["F (Client)"]["B (Hub)"] = 35

    return full_matrix

TSP_MATRIX = get_tsp_matrix()
