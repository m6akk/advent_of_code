
def check_neighbour(grid, height, node):
    
    if node[0] < 0 or node[0] >= len(grid) or node[1] < 0 or node[1] >= len(grid[0]):
        return False
    
    else:
        height2 = ord(grid[node[0]][node[1]])

        if height + 1 >= height2:
            return True 
        else:
            return False

    
    



def find_neighbours(grid, node):

    neighbours = []
    height = ord(grid[node[0]][node[1]])

    if node == [0,0]:
        return [[0,1], [1,0]]  
      

    if check_neighbour(grid, height, [node[0], node[1]-1]):
        neighbours.append([node[0], node[1]-1])
    if check_neighbour(grid, height, [node[0]-1, node[1]]):
        neighbours.append([node[0]-1, node[1]])
    if check_neighbour(grid, height, [node[0] , node[1]+1]):
        neighbours.append([node[0], node[1]+1])
    if check_neighbour(grid, height, [node[0]+1, node[1]]):
        neighbours.append([node[0]+1, node[1]])


    return neighbours



# def find_path(grid, queue, visited):

#     node = queue.pop(0)

#     if node == [2,5]:
#         return 

#     visited.append(node)

#     neighbours = find_neighbours(grid, node)

#     for neighbour in neighbours:
#         if neighbour not in visited:
#             queue.append(neighbour)

#     find_path(grid, queue, visited)



grid = [
    ['S','a','b','q','p','o','n','m'],
    ['a','b','c','r','y','x','x','l'],
    ['a','c','c','s','z','E','x','k'],
    ['a','c','c','t','u','v','w','j'],
    ['a','b','d','e','f','g','h','i']
    ]


start = [0,0]
end = [2,5]

queue = []
visited = []


queue.append(start)
steps = 0

while queue:
    node = queue.pop(0)

    steps = steps+1
    print(node)

    if node == [2,5]:
        print("Kraj")
        print(steps)
        break

    visited.append(node)

    neighbours = find_neighbours(grid, node)

    if neighbours:
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
    
    print(queue)
    print()

    
        
# print(find_neighbours(grid, [0,1]))
