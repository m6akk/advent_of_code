

def find_paths(graph, start, end):

    paths = []

    def dfs(current, path, visited_small_caves):

        if current == end:
            paths.append(path)
            return
        
        for neighbour in graph[current]:

            if neighbour.islower and neighbour in visited_small_caves:
                continue

            new_visited_small_caves = visited_small_caves.copy()
            if neighbour.islower():
                new_visited_small_caves.add(neighbour)

            dfs(neighbour, path + [neighbour], new_visited_small_caves)
    

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


visited_small_caves = set()


paths = find_paths(graph, 'start', 'end')

for path in paths:
    print(path)