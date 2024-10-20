import numpy as np
import networkx as nx
import multiprocessing
from collections import deque
from typing import Union

def Floyd(Graph : Union[nx.Graph, nx.DiGraph]) -> np.ndarray:
    """返回最短路矩阵, 使用Floyd算法

    Args:
        Graph (Union[nx.Graph, nx.DiGraph]): networkx.Graph / networkx.DiGraph 表示的图

    Returns:
        np.ndarray: 最短路矩阵
    """
    # 初始化
    n = len(Graph)
    dist = np.array([[float('inf') for i in range(n)] for j in range(n)])
    for i in range(n):
        dist[i][i] = 0
    for edge in Graph.edges():
        if isinstance(Graph, nx.DiGraph):
            dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
        else:
            dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
            dist[edge[1]][edge[0]] = Graph[edge[0]][edge[1]]['weight']
    # Floyd算法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def update_distance(shared_dist, n, il, ir, jl, jr, k):
    if ir <= il or jr <= jl:
        return
    
    # 将共享内存的 dist 重新映射为 NumPy 数组
    dist = np.frombuffer(shared_dist).reshape((n, n))

    # 更新距离，带有 k 十字写保护
    for i in range(il, ir):
        for j in range(jl, jr):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    

def ParallelFloyd(Graph: Union[nx.Graph, nx.DiGraph]) -> np.ndarray:
    """返回最短路矩阵, 使用并行Floyd算法

    Args:
        Graph (Union[nx.Graph, nx.DiGraph]): networkx.Graph / networkx.DiGraph 表示的图

    Returns:
        np.ndarray: 最短路矩阵
    """
    # 初始化
    n = len(Graph)
    
    # 初始化共享的 dist 数组为一维列表，方便并行进程共享
    dist = np.array([[float('inf') for i in range(n)] for j in range(n)])
    for i in range(n):
        dist[i][i] = 0
    for edge in Graph.edges():
        if isinstance(Graph, nx.DiGraph):
            dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
        else:
            dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
            dist[edge[1]][edge[0]] = Graph[edge[0]][edge[1]]['weight']
    
    # 将 dist 转换为共享内存中的可变列表
    shared_dist = multiprocessing.Array('d', dist.flatten(), lock=False)

    # 多进程并行执行 Floyd 算法
    for k in range(n):
        processes = []
        tasks = [
            (shared_dist, n, 0, k, 0, k, k),
            (shared_dist, n, k+1, n, 0, k, k),
            (shared_dist, n, 0, k, k+1, n, k),
            (shared_dist, n, k+1, n, k+1, n, k)
        ]
        for task in tasks:
            p = multiprocessing.Process(target=update_distance, args=task)
            processes.append(p)
            p.start()
        for p in processes:
            p.join()


    # 任务完成后，将共享的 dist 恢复为 NumPy 二维数组
    return np.array(shared_dist).reshape((n, n))

def FloydGetPath(Graph : Union[nx.Graph, nx.DiGraph], start : int, end : int) -> (list, float):
    """返回最短路列表&路径长度, 使用Floyd算法

    Args:
        Graph (Union[nx.Graph, nx.DiGraph]): networkx.Graph / networkx.DiGraph 表示的图

    Returns:
        np.ndarray: 最短路矩阵
    """
    # 初始化
    n = len(Graph)
    dist = np.array([[float('inf') for i in range(n)] for j in range(n)])
    next_node = np.full((n, n), np.nan, dtype=object)
    for i in range(n):
        dist[i][i] = 0
    for edge in Graph.edges():
        if isinstance(Graph, nx.DiGraph):
            dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
            next_node[edge[0]][edge[1]] = (edge[1], dist[edge[0]][edge[1]])
        else:
            dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
            dist[edge[1]][edge[0]] = Graph[edge[0]][edge[1]]['weight']
            next_node[edge[0]][edge[1]] = (edge[1], dist[edge[0]][edge[1]])
            next_node[edge[1]][edge[0]] = (edge[0], dist[edge[1]][edge[0]])
    # Floyd算法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    shortest_dict = dist[start][end]

    # 建立路径
    if not isinstance(next_node[start][end], tuple):
        return [], float('inf')
    path = []
    while start != end:
        path.append((start, next_node[start][end][0], int(next_node[start][end][1])))
        start = next_node[start][end][0]
        
    return path, shortest_dict



def Dijkstra(Graph: Union[nx.Graph, nx.DiGraph], start: int):
    n = len(Graph)
    dist = np.array([float('inf') for _ in range(n)])
    dist[start] = 0
    visited = [False for _ in range(n)]
    
    for _ in range(n):
        min_dist = float('inf')
        u = -1
        for j in range(n):
            if not visited[j] and dist[j] < min_dist:
                u = j
                min_dist = dist[j]
        if u == -1:  # 所有可达节点已访问
            break
        visited[u] = True
        for v in range(n):
            if not visited[v]:
                edge_data = Graph.get_edge_data(u, v)
                if edge_data is not None:
                    weight = edge_data.get('weight', float('inf'))
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
    return dist

def BellmanFord(Graph: Union[nx.Graph, nx.DiGraph], start: int):
    n = len(Graph)
    dist = np.array([float('inf') for _ in range(n)])
    dist[start] = 0
    if isinstance(Graph, nx.DiGraph):
        for _ in range(n):
            for u, v in Graph.edges():
                if dist[u] + Graph[u][v]['weight'] < dist[v]:
                    dist[v] = dist[u] + Graph[u][v]['weight']
    elif isinstance(Graph, nx.Graph):
        for _ in range(n):
            for u, v in Graph.edges():
                if dist[u] + Graph[u][v]['weight'] < dist[v]:
                    dist[v] = dist[u] + Graph[u][v]['weight']
                if dist[v] + Graph[u][v]['weight'] < dist[u]:
                    dist[u] = dist[v] + Graph[u][v]['weight']
    return dist

def BellmanFoldSPFA(Graph : nx.Graph, start : int):
    # 初始化
    n = len(Graph)
    dist = np.array([float('inf') for i in range(n)])
    vis = np.zeros(n, dtype=bool)
    q = deque()

    dist[start] = 0
    q.append(start)
    vis[start] = True

    # Bellman-Fold算法
    while len(q) > 0:
        u = q.popleft()
        for v in Graph.neighbors(u):
            if dist[u] + Graph[u][v]['weight'] < dist[v]:
                dist[v] = dist[u] + Graph[u][v]['weight']
                q.append(v) 
    return dist

# if __name__ == '__main__':
#     G = nx.Graph()
#     G.add_edge(0, 1, weight=1)
#     G.add_edge(1, 2, weight=2)
#     G.add_edge(2, 3, weight=3)
#     G.add_edge(3, 0, weight=4)
#     G.add_edge(0, 2, weight=5)
#     G.add_edge(1, 3, weight=6)
#     G.add_edge(4, 5, weight=7)
#     print(BellmanFord(G, 3))