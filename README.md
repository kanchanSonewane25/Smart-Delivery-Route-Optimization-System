DAA Project: Smart Delivery Route Optimization System

This project is a Python application that demonstrates three core graph algorithms used in logistics and network optimization. It provides a graphical user interface (GUI) built with Tkinter to visualize the results of each algorithm on a predefined delivery network.

Problem Definition

A delivery company wants to optimize its operations in three ways:

Build Lowest-Cost Network: Determine the cheapest way to build a road network that connects all its delivery hubs and client locations.

Find Shortest Paths: Compute the shortest delivery routes from the central warehouse to all other destinations, considering potential costs.

Plan Round-Trip: Find the most efficient round-trip route for a delivery truck that must visit all destinations and return to the warehouse.

Algorithms Used & Time Complexity

This project implements and visualizes the following three algorithms:

1. Kruskal’s Algorithm (Minimum Spanning Tree)

Purpose: Solves the "Build Lowest-Cost Network" problem. It finds the Minimum Spanning Tree (MST) of the graph, which is the set of edges (roads) that connects all nodes (locations) with the minimum possible total cost (construction cost).

Time Complexity: O(E log V), where E is the number of potential roads and V is the number of locations. This is highly efficient.

2. Bellman-Ford Algorithm (Shortest Path)

Purpose: Solves the "Find Shortest Paths" problem. It finds the shortest path from a single source (the Warehouse) to all other nodes in the graph.

Why Bellman-Ford? Unlike Dijkstra's algorithm, Bellman-Ford can handle edges with negative weights (which could represent a "subsidy" or "rebate" on a route). It can also detect negative-weight cycles (an impossible situation where a route gets infinitely cheaper).

Time Complexity: O(VE), where V is the number of locations and E is the number of roads.

3. Travelling Salesman Problem (TSP) - Brute-Force

Purpose: Solves the "Plan Round-Trip" problem. It finds the shortest possible route that visits every single destination exactly once and returns to the starting point (the Warehouse).

Time Complexity: O(N!), where N is the number of destinations to visit. This is a brute-force solution that checks every single possible permutation of routes. It is not efficient and becomes unusable (will freeze the app) with more than ~10 destinations.

Project File Structure

main_delivery.py: The main file. Runs the Tkinter application, creates the GUI, and handles button clicks to trigger the algorithms.

graph_data.py: Contains the raw data for the graph, including node coordinates for drawing and the list of edges with their costs. You can edit this file to change the map!

algorithms.py: Contains the clean, separated Python implementations for Kruskal's, Bellman-Ford's, and the brute-force TSP.

README.md: This file.

How to Run

Make sure you have Python 3 installed.

Save all four files (main_delivery.py, graph_data.py, algorithms.py, README.md) in the same directory.

Open a terminal or command prompt and navigate to that directory.

Run the main file:

python main_delivery.py


The GUI window will open. Use the buttons on the left to run each algorithm and see the visualization and output.
