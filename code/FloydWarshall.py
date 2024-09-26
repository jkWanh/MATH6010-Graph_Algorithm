from networkx import Graph
def Floyd(Graph : Graph):
    # 初始化
    n = len(Graph)
    dist = [[float('inf') for i in range(n)] for j in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for edge in Graph.edges():
        dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
        dist[edge[1]][edge[0]] = Graph[edge[0]][edge[1]]['weight']
    # Floyd算法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
