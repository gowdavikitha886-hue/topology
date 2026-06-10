def warshall(graph):
    n = len(graph)

    # Apply Warshall's Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])

    return graph


# Input
n = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Find transitive closure
result = warshall(graph)

# Output
print("\nTransitive Closure Matrix:")
for row in result:
    for value in row:
        print(value, end=" ")
    print()