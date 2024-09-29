import random
import os
import json
import sys
import importlib

import pytest
import networkx as nx

from networkx.readwrite import json_graph
sys.path.append('code')
ioProcess = importlib.import_module('ioProcess')

def check_negative_cycle(G: nx.Graph) -> bool:
    """检查图G是否含有负权重环

    Args:
        G (nx.Graph): 输入图G, 同时支持无向图和有向图

    Returns:
        bool: 是否含有负权重环
    """
    # 无向图
    if not isinstance(G, nx.DiGraph):
        for u, v in G.edges():
            try:
                if G[u][v]['weight'] < 0:
                    return True
            except KeyError:
                print(f"Edge {u} - {v} does not have weight attribute")
                exit(1)
        return False
    
    # 有向图
    n = len(G.nodes)
    dist = [0] * n
    flag = False

    for _ in range(n):
        flag = False
        for u, v in G.edges():
            try:
                if dist[u] + G[u][v]['weight'] < dist[v]:
                    dist[v] = dist[u] + G[u][v]['weight']
                    flag = True
            except KeyError:
                print(f"Edge {u} -> {v} does not have weight attribute")
                exit(1)
        if not flag:
            break
    return flag
    
def generate_class1_random_graph(n: int, temperature: float, directed: bool = False) -> nx.Graph:
    """生成等价类1：非负边权重图（含有向图&无向图，边权重$[0,100]$）

    Args:
        n (int): 点数
        temperature (float): 生成图的边概率
        directed (bool, optional): 是否有向图. Defaults to False.

    Returns:
        nx.Graph: 随机生成等价类1的图
    """
    G = nx.erdos_renyi_graph(n, temperature, directed=directed)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(0, 100)
    return G

def generate_class2_random_graph(n: int, temperature: float) -> nx.DiGraph:
    """生成等价类2：含负边权重图（含负权重边的有向图，边权重$[-50,50]$，无负权重环）

    Args:
        n (int): 点数
        temperature (float): 生成图的边概率

    Returns:
        nx.DiGraph: 随机生成等价类2的图
    """
    G = nx.erdos_renyi_graph(n, temperature, directed=True)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(-50, 50)
    while check_negative_cycle(G):
        (u, v, weight) = random.choice([(u, v, data['weight']) for u, v, data in G.edges(data=True) if data['weight'] < 0])
        G[u][v]['weight'] = random.randint(0, 50)
    return G

def generate_class3_random_graph(n: int, directed: bool = False) -> nx.Graph:
    """生成等价类3：非负边权重稀疏图（含有向图&无向图，边权重$[0,100]$，$|E| < 5\cdot|V|$）

    Args:
        n (int): 点数
        directed (bool, optional): 是否有向图. Defaults to False.

    Returns:
        nx.Graph: 随机生成等价类3的图
    """
    m = random.randint(5, 50) * n // 10
    G = nx.gnm_random_graph(n, m, directed=directed)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(0, 100)
    return G

def generate_class4_random_graph(n: int, directed: bool = False) -> nx.Graph:
    """生成等价类4: 非负边权重稠密图（含有向图&无向图，边权重$[0,100]$，$|E| > 0.5\cdot|V|^2$）

    Args:
        n (int): 点数
        directed (bool, optional): 是否有向图. Defaults to False.

    Returns:
        nx.Graph: 随机生成等价类4的图
    """
    m = random.randint(n * n // 2, n * n)
    G = nx.gnm_random_graph(n, m, directed=directed)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(0, 100)
    return G

def generate_class5_random_graph(n: int) -> nx.DiGraph:
    """生成等价类5: 含负边权重稀疏图（含负权重边有向图，边权重$[-50,50]$，$|E| < 5\cdot|V|$，无负权重环）

    Args:
        n (int): 点数

    Returns:
        nx.DiGraph: 随机生成等价类5的图
    """
    m = random.randint(5, 50) * n // 10
    G = nx.gnm_random_graph(n, m, directed=True)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(-50, 50)
    while check_negative_cycle(G):
        (u, v, weight) = random.choice([(u, v, data['weight']) for u, v, data in G.edges(data=True) if data['weight'] < 0])
        G[u][v]['weight'] = random.randint(0, 50)
    return G

def generate_class6_random_graph(n: int) -> nx.DiGraph:
    """生成等价类6: 含负边权重稠密图（含负权重边有向图，边权重$[-50,50]$，$|E| > 0.5\cdot|V|^2$，无负权重环）

    Args:
        n (int): 点数

    Returns:
        nx.DiGraph: 随机生成等价类6的图
    """
    m = random.randint(n * n // 2, n * n)
    G = nx.gnm_random_graph(n, m, directed=True)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(-50, 50)
    while check_negative_cycle(G):
        (u, v, weight) = random.choice([(u, v, data['weight']) for u, v, data in G.edges(data=True) if data['weight'] < 0])
        G[u][v]['weight'] = random.randint(0, 50)
    return G

def generate_class7_random_graph(n: int, temperature: float, directed: bool = False ) -> nx.DiGraph:
    """生成等价类7: 负权重环图（含有向图&无向图，边权重$[-50,50]$且至少有向图有一个负权重环, 无向图至少含有一条负权重边）

    Args:
        n (int): 点数
        temperature (float): 生成图的边概率
        directed (bool, optional): 是否有向图. Defaults to False.

    Returns:
        nx.DiGraph: 随机生成等价类7的图
    """
    G = nx.erdos_renyi_graph(n, temperature, directed=directed)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(-50, 50)
    while not check_negative_cycle(G):
        (u, v) = random.choice([(u, v, data['weight']) for u, v, data in G.edges(data=True) if data['weight'] > 0])
        G[u][v]['weight'] = random.randint(-50, -1)
    return G


def save_graph_list_to_json(graph_list: list, file_path: str):
    """将图列表以JSON格式存储到文件

    Args:
        graph_list (list): 要存储的图列表
        file_path (str): 存储文件的路径
    """
    data = [json_graph.node_link_data(G) for G in graph_list]
    with open(file_path, 'w') as f:
        json.dump(data, f)

def load_graph_list_from_json(file_path: str) -> list:
    """从JSON文件读取图列表

    Args:
        file_path (str): JSON文件的路径

    Returns:
        list: 读取的图列表
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    graph_list = [json_graph.node_link_graph(graph_data) for graph_data in data]
    return graph_list

def generate_test_cases():
    test_cases = []

    for i in range(10):
        n = random.randint(5, 20)
        temperature = random.random()
        temperature = 1.0 if temperature == 0 else temperature
        directed = random.choice([True, False])
        G = generate_class1_random_graph(n, temperature, directed)
        test_cases.append(G)

    # 保存测试用例
    os.makedirs('test/sample_test_cases', exist_ok=True)
    save_graph_list_to_json(test_cases, 'test/sample_test_cases/sample_test_cases.json')

if __name__ == "__main__":
    # generate_test_cases()
    # 手工负环图
    # edges = [
    #     (0, 1, { 'weight': 1 }),
    #     (1, 2, { 'weight': 2 }),
    #     (2, 3, { 'weight': 3 }),
    #     (3, 0, { 'weight': -9 }),
    # ]
    # G = nx.DiGraph()
    # G.add_edges_from(edges)
    # print(check_negative_cycle(G))  # True
    generate_test_cases()
    graph_list = load_graph_list_from_json('test/sample_test_cases/sample_test_cases.json')
    i = 0
    for G in graph_list:
        i += 1
        ioProcess.base_file_name = f'randomGraph{i}'
        ioProcess.renderGraph(G)
        

