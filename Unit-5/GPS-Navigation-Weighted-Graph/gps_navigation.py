import heapq

# A small sample city map. Distances are examples in kilometres.
CITY_MAP = {
    "College": {"Bus Stand": 2, "Market": 4},
    "Bus Stand": {"College": 2, "Market": 1, "Hospital": 5},
    "Market": {"College": 4, "Bus Stand": 1, "Railway Station": 3, "Hospital": 2},
    "Hospital": {"Bus Stand": 5, "Market": 2, "Railway Station": 2, "Airport": 8},
    "Railway Station": {"Market": 3, "Hospital": 2, "Airport": 5},
    "Airport": {"Hospital": 8, "Railway Station": 5},
}


def dijkstra(graph, start):
    distances = {place: float("inf") for place in graph}
    parents = {place: None for place in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_place = heapq.heappop(priority_queue)

        # Ignore an old queue entry if a shorter distance was found later.
        if current_distance > distances[current_place]:
            continue

        for neighbour, road_distance in graph[current_place].items():
            new_distance = current_distance + road_distance
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                parents[neighbour] = current_place
                heapq.heappush(priority_queue, (new_distance, neighbour))

    return distances, parents


def build_route(parents, destination):
    route = []
    current = destination
    while current is not None:
        route.append(current)
        current = parents[current]
    route.reverse()
    return route


def main():
    print("GPS / Navigation - Shortest Route Demo")
    print("Available places:", ", ".join(CITY_MAP.keys()))
    start = input("Enter starting place: ").strip().title()
    destination = input("Enter destination: ").strip().title()

    if start not in CITY_MAP or destination not in CITY_MAP:
        print("Place not found. Please use one of the listed place names.")
        return

    distances, parents = dijkstra(CITY_MAP, start)
    if distances[destination] == float("inf"):
        print("No route is available.")
        return

    route = build_route(parents, destination)
    print("Shortest route:", " -> ".join(route))
    print(f"Total distance: {distances[destination]} km")


if __name__ == "__main__":
    main()
