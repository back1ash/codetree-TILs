n, m = map(int, input().split())

visited = [0 for _ in range(n+1)]
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(now):
    for vertex in range(n):
        if graph[now][vertex] and not visited[vertex]:
            visited[vertex] = 1
            dfs(vertex)

dfs(1)
print(visited.count(1)-1 if visited.count(1) > 0 else 0)