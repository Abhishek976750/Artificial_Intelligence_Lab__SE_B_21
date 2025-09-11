from collections import deque

def bfs(maze, start, end):
   
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([start])  
    visited = set(start)    

    while queue:
        current = queue.popleft()
        if current == end:
            return True  

        for direction in directions:
            
            next_cell = (current[0] + direction[0], current[1] + direction[1])

            
            if (0 <= next_cell[0] < len(maze) and
                    0 <= next_cell[1] < len(maze[0]) and
                    maze[next_cell[0]][next_cell[1]] != '#' and
                    next_cell not in visited):
                queue.append(next_cell)
                visited.add(next_cell)

    return False  


maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '#', '.'],
    ['#', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '.', '.'],
    ['.', '', '.', '.', '.', '#', '.'],
    ['#', '#', '#', '#', '#', '#', '#'],
    ['.', '#', 'E', '#', '.', '.', '.'],
]

start = (0, 0)  
end = (6, 6)    


path = bfs(maze, start, end)

if path:
            print(path_exists)
            print("Path is found")
else:
            print("Path is not found")            



