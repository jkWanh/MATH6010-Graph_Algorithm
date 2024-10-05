import random
import os

import networkx as nx
import tests.test as test

from typing import Union

def generate_class1_random_graph(n: int, temperature: float, directed: bool = False) -> Union[nx.Graph, nx.DiGraph]:
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
    while test.check_negative_cycle(G):
        (u, v, weight) = random.choice([(u, v, data['weight']) for u, v, data in G.edges(data=True) if data['weight'] < 0])
        G[u][v]['weight'] = random.randint(0, 50)
    return G

def generate_class3_random_graph(n: int, directed: bool = False) -> Union[nx.Graph, nx.DiGraph]:
    """生成等价类3：非负边权重稀疏图（含有向图&无向图，边权重$[0,100]$，$|E| < 5\cdot|V|$）

    Args:
        n (int): 点数
        directed (bool, optional): 是否有向图. Defaults to False.

    Returns:
        nx.Graph: 随机生成等价类3的图
    """
    m = random.randint(5, 30) * n // 10
    G = nx.gnm_random_graph(n, m, directed=directed)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(0, 100)
    return G

def generate_class4_random_graph(n: int, directed: bool = False) -> Union[nx.Graph, nx.DiGraph]:
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
    m = random.randint(5, 30) * n // 10
    G = nx.gnm_random_graph(n, m, directed=True)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(-50, 50)
    while test.check_negative_cycle(G):
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
    while test.check_negative_cycle(G):
        (u, v, weight) = random.choice([(u, v, data['weight']) for u, v, data in G.edges(data=True) if data['weight'] < 0])
        G[u][v]['weight'] = random.randint(0, 50)
    return G

def generate_class7_random_graph(n: int, temperature: float, directed: bool = False ) -> Union[nx.Graph, nx.DiGraph]:
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
    while not test.check_negative_cycle(G):
        (u, v, weight) = random.choice([(u, v, data['weight']) for u, v, data in G.edges(data=True) if data['weight'] >= 0])
        G[u][v]['weight'] = random.randint(-50, -1)
    return G

def generate_test_cases(case_type: str = 'class1', num: int = 10):

    valid_case_types = [f'class{i}' for i in range(1, 9)]
    test_cases = []

    if case_type not in valid_case_types:
        raise ValueError(f"Invalid case type: {case_type}")
    elif case_type == 'class1':
        for i in range(num):
            n = random.randint(5, 30)
            temperature = random.random()
            temperature = 1.0 if temperature == 0 else temperature
            directed = random.choice([True, False])
            G = generate_class1_random_graph(n, temperature, directed)
            test_cases.append(G)
    elif case_type == 'class2':
        for i in range(num):
            n = random.randint(5, 30)
            temperature = random.random()
            temperature = 1.0 if temperature == 0 else temperature
            G = generate_class2_random_graph(n, temperature)
            test_cases.append(G)
    elif case_type == 'class3':
        for i in range(num):
            n = random.randint(5, 30)
            directed = random.choice([True, False])
            G = generate_class3_random_graph(n, directed)
            test_cases.append(G)
    elif case_type == 'class4':
        for i in range(num):
            n = random.randint(5, 20)
            directed = random.choice([True, False])
            G = generate_class4_random_graph(n, directed)
            test_cases.append(G)
    elif case_type == 'class5':
        for i in range(num):
            n = random.randint(5, 30)
            G = generate_class5_random_graph(n)
            test_cases.append(G)
    elif case_type == 'class6':
        for i in range(num):
            n = random.randint(5, 30)
            G = generate_class6_random_graph(n)
            test_cases.append(G)
    elif case_type == 'class7':
        for i in range(num):
            n = random.randint(5, 30)
            temperature = random.random()
            temperature = 1.0 if temperature == 0 else temperature
            directed = random.choice([True, False])
            G = generate_class7_random_graph(n, temperature, directed)
            test_cases.append(G)
    elif case_type == 'class8':

        case7Num = max(num//10, 1) 
        num = max(num-case7Num, 0)
        for i in range(case7Num):
            n = random.randint(5, 30)
            temperature = random.random()
            temperature = 1.0 if temperature == 0 else temperature
            directed = random.choice([True, False])
            G = generate_class7_random_graph(n, temperature, directed)
            test_cases.append(G)

        case6Num =random.randint(1, max((num * 2) // 4, 1))
        num = max(num-case6Num, 0)
        for i in range(case6Num):
            n = random.randint(5, 30)
            G = generate_class6_random_graph(n)
            test_cases.append(G) 

        case5Num = random.randint(1, max((num * 2) // 3, 1))
        num = max(num-case5Num, 0)
        for i in range(num):
            n = random.randint(5, 30)
            G = generate_class5_random_graph(n)
            test_cases.append(G)

        case4Num = random.randint(1, max(num - 1, 1))
        num = max(num-case4Num, 0)
        for i in range(case4Num):
            n = random.randint(5, 20)
            directed = random.choice([True, False])
            G = generate_class4_random_graph(n, directed)
            test_cases.append(G)
        
        case3Num = max(1, num)
        for i in range(case3Num):
            n = random.randint(5, 30)
            directed = random.choice([True, False])
            G = generate_class3_random_graph(n, directed)
            test_cases.append(G)

    # 保存测试用例
    os.makedirs(f'data/sample_test_cases/{case_type}', exist_ok=True)
    scale = "lite" if num <= 10 else "medium"
    scale = "large" if num >= 50 else scale
    count = 0
    for fileName in os.listdir(f'data/sample_test_cases/{case_type}'):
        if fileName.startswith(f'{scale}_{case_type}_test_cases'):
            count += 1
    test.save_graph_list_to_json(test_cases, f'data/sample_test_cases/{case_type}/{scale}_{case_type}_test_cases{count+1}.json')