heightmap = [
    [2,1,9,9,9,4,3,2,1,0],
    [3,9,8,7,8,9,4,9,2,1],
    [9,8,5,6,7,8,9,8,9,2],
    [8,7,6,7,8,9,6,7,8,9],
    [9,8,9,9,9,6,5,6,7,8]
]

low_points = []
risk_level_sum = 0

for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        current_height = heightmap[i][j]
        is_low_point = True
        
        # check if current location is lower than all adjacent locations
        if i > 0 and current_height >= heightmap[i-1][j]:
            is_low_point = False
        if i < len(heightmap)-1 and current_height >= heightmap[i+1][j]:
            is_low_point = False
        if j > 0 and current_height >= heightmap[i][j-1]:
            is_low_point = False
        if j < len(heightmap[0])-1 and current_height >= heightmap[i][j+1]:
            is_low_point = False
            
        # add risk level to sum if location is a low point
        if is_low_point:
            risk_level = current_height + 1
            risk_level_sum += risk_level
            low_points.append((i,j,risk_level))

# print low points and risk level sum
print("Low points:", low_points)
print("Risk level sum:", risk_level_sum)