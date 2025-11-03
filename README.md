# DAA: Delivery Route Optimization

A command-line Python application demonstrating core graph algorithms for logistics optimization.

## Problem Definition

1.  Build Network: Find the cheapest way to connect all delivery hubs.
2.  Shortest Paths: Find the shortest delivery routes from the warehouse to all other locations.
3.  Round-Trip: Find the most efficient route to visit all destinations and return to the warehouse.

---

## Algorithms

* **Kruskal’s Algorithm (Minimum Spanning Tree)**
    * Solves the "Build Network" problem.
    * Time Complexity: $O(E \log V)$

* **Bellman-Ford Algorithm (Shortest Path)**
    * Solves the "Shortest Paths" problem, handling negative weights.
    * Time Complexity: $O(VE)$

* **Travelling Salesman Problem (TSP) - Brute-Force**
    * Solves the "Round-Trip" problem.
    * Time Complexity: O(N!)
