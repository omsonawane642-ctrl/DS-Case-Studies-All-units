# Case Study 1: GPS / Navigation System Using a Weighted Graph

## Introduction
A GPS or navigation application helps a person travel from one place to another. A city can be represented as a graph, where places are vertices and roads are edges. Each road has a weight, such as distance in kilometres. A shortest-path algorithm can find a route with the smallest total distance.

## Aim
To model a small city map as a weighted graph and use Dijkstra's algorithm to find the shortest path between two locations.

## Objectives
- Understand weighted graphs and their use in navigation.
- Represent places and roads using an adjacency list.
- Apply Dijkstra's shortest-path algorithm.
- Display the shortest route and its total distance.
- Understand the time and space complexity of the algorithm.

## Problem Statement
A user wants to travel from a starting location to a destination. The map contains different places connected by roads of different lengths. The program should find the route with the minimum total distance.

## Data Structure and Algorithm
- **Vertex:** a place in the city.
- **Edge:** a road connecting two places.
- **Weight:** the distance of a road in kilometres.
- **Adjacency list:** stores each place and its connected places.
- **Dijkstra's algorithm:** finds shortest paths from a source when all edge weights are non-negative.

This is a small educational map. Real navigation systems may also consider traffic, road closures, turn restrictions, travel time, and live map data.

## Algorithm
1. Store the city roads and their distances in an adjacency list.
2. Set the starting place distance to zero and all other distances to infinity.
3. Use a priority queue to select the place with the smallest known distance.
4. Check each connected road and update a distance if a shorter route is found.
5. Repeat until the destination is reached or no reachable places remain.
6. Reconstruct and print the shortest route and its total distance.

## Pseudocode
```text
DIJKSTRA(graph, source):
    distance of every vertex = infinity
    parent of every vertex = none
    distance[source] = 0
    priority queue = (0, source)

    while priority queue is not empty:
        (current_distance, current_vertex) = remove smallest item
        if current_distance is outdated:
            continue

        for each neighbour and road_weight:
            new_distance = current_distance + road_weight
            if new_distance < distance[neighbour]:
                distance[neighbour] = new_distance
                parent[neighbour] = current_vertex
                add (new_distance, neighbour) to priority queue

    return distance, parent
```

## Sample Map
The sample program contains these locations: College, Bus Stand, Market, Hospital, Railway Station, and Airport. The road distances are sample values for demonstration only.

## How to Run
```bash
python gps_navigation.py
```

Enter a starting place and a destination when prompted. Use the place names printed by the program.

## Time and Space Complexity
Using an adjacency list and a binary heap priority queue, Dijkstra's algorithm is commonly described as **O((V + E) log V)**. The graph and supporting arrays require **O(V + E)** space, where V is the number of places and E is the number of roads.

## Advantages
- Finds a shortest route by distance for non-negative road weights.
- An adjacency list is suitable for maps where each place connects to only some nearby places.
- The route can be updated if the road data changes and the algorithm is run again.

## Limitations
- The sample uses fixed road distances.
- It does not use live traffic or GPS sensor data.
- Dijkstra's algorithm is not designed for negative edge weights.

## Conclusion
In this case study, I learned how a city map can be represented as a weighted graph. Dijkstra's algorithm helps find the shortest path between two locations by comparing the total distances of possible routes.

## References
- Python documentation: https://docs.python.org/3/
- Dijkstra's shortest-path algorithm: standard graph algorithm study material.
