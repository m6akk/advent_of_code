def find_paths(graph, start, end, visited_small_caves=set()):
    """
    Find all distinct paths from start to end in the given graph,
    avoiding revisiting small caves.
    """
    # Initialize the list of paths found
    paths = []

    def dfs(current, path, visited_small_caves):
        # If we reach the end node, add the current path to the list of paths found
        if current == end:
            paths.append(path)
            return

        # Explore all neighboring nodes that haven't been visited yet
        for neighbor in graph[current]:
            # If the neighbor is a small cave and has already been visited, skip it
            if neighbor.islower() and neighbor in visited_small_caves:
                continue

            # Update the set of visited small caves if we visit a new one
            new_visited_small_caves = visited_small_caves.copy()
            if neighbor.islower():
                new_visited_small_caves.add(neighbor)

            # Recursively explore the neighbor
            dfs(neighbor, path + [neighbor], new_visited_small_caves)

    # Start the DFS from the start node
    dfs(start, [start], visited_small_caves)

    return paths





graph = {
    'start': ['A', 'b'],
    'A': ['c', 'b', 'end'],
    'b': ['A', 'd', 'end'],
    'c': ['A'],
    'd': ['b'],
    'end': ['A', 'b']
}


paths = find_paths(graph, 'start', 'end')
for path in sorted(paths):
    print(','.join(path))
