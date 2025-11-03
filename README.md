# Smart Delivery Route Optimization System

To design and implement a delivery route optimization system using algorithmic techniques to minimize delivery costs, find shortest routes considering traffic delays, and plan an optimal round-trip delivery path.

## Problem Definition

A delivery company wants to optimize its operations:
Build the lowest-cost delivery road network.
Compute the shortest delivery paths from the warehouse to all destinations.
Plan the most efficient round-trip route for a delivery truck visiting all locations.

## Algorithms Used
Kruskal’s Algorithm (MST): Builds a minimum-cost road network between delivery hubs.

Bellman-Ford Algorithm: Finds the shortest paths from the warehouse to all destinations, even with negative edge weights.

Travelling Salesman Problem (TSP): Determines the shortest possible route that visits all destinations exactly once.

## Time Complexity Analysis
Kruskal’s Algorithm	- O(E log V)	- Build low-cost road network
Bellman-Ford Algorithm - O(VE) - Compute shortest paths from warehouse
TSP (Brute Force) - O(N!) - Find optimal delivery route
