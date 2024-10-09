import random
import os
import json
import sys
import importlib

import pytest
import networkx as nx
import tests.test_cases as tc
import numpy as np
import codes.ioProcess as ioProcess

from networkx.readwrite import json_graph
from codes.algorithm import Floyd
from codes.ioProcess import renderGraph

class TestClass:
    def __init__(self, test_cases_file: str = None) -> None:
        self.graph_list = []
        self.shortest_path_matrix = []
        
def check_edge_weight(G: nx.Graph) -> bool:
    """检查图G的边是否有weight属性

    Args:
        G (nx.Graph): 输入图G

    Returns:
        bool: 是否有type为int或float的weight属性
    """
    for u, v in G.edges():
        if 'weight' not in G[u][v] or not isinstance(G[u][v]['weight'], (int, float)):
            return False
    return True

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

def save_graph_list_to_json(graph_list: list, file_path: str):
    """将图列表以JSON格式存储到文件, 用于测试用例

    Args:
        graph_list (list): 要存储的图列表
        file_path (str): 存储文件的路径
    """
    data_list = []
    for G in graph_list:
        if not isinstance(G, nx.Graph):
            raise ValueError("Input graph_list should contain networkx.Graph objects")
        if check_edge_weight(G) and (not check_negative_cycle(G)):
            short_path_matrix = Floyd(G)
            short_path_matrix = short_path_matrix.tolist()
            short_path_matrix = [[str(x) if np.isinf(x) or np.isnan(x) else x for x in row] for row in short_path_matrix]
        else:
            short_path_matrix = None
        data = {
            'graph': json_graph.node_link_data(G),
            'shortest_path_matrix': short_path_matrix
        }
        data_list.append(data)
    
    try:
        with open(file_path, 'w') as f:
            json.dump(data_list, f)
    except Exception as e:
        raise e

def load_graph_list_from_json(file_path: str) -> list:
    """从JSON文件读取图列表

    Args:
        file_path (str): JSON文件的路径

    Returns:
        list: 读取的图列表
    """
    with open(file_path, 'r') as f:
        data_list_json = json.load(f)
    data_list = []
    for data_json in data_list_json:
        graph = json_graph.node_link_graph(data_json['graph'])
        shortest_path_matrix = data_json['shortest_path_matrix']
        if shortest_path_matrix is not None:
            shortest_path_matrix = [[float(x) if isinstance(x, str) and (x == 'inf' or x == '-inf' or x == 'nan') else x for x in row] for row in shortest_path_matrix]
            shortest_path_matrix = np.array(shortest_path_matrix)
        data = {
            'graph': graph,
            'shortest_path_matrix': shortest_path_matrix
        }
        data_list.append(data)
    return data_list



if __name__ == "__main__":
    # generate_test_cases()
    # graph_list = load_graph_list_from_json('tests/sample_test_cases/sample_test_cases.json')
    # i = 0
    # for G in graph_list:
    #     i += 1
    #     ioProcess.base_file_name = f'randomGraph{i}'
    #     ioProcess.renderGraph(G)
    # generate_test_cases()
    tc.generate_test_cases('class8', random.randint(11, 50))
    # graph_list = load_graph_list_from_json('data/sample_test_cases/sample_test_cases.json')
    # i = 0
    # for data in graph_list:
    #     i += 1
    #     G = data['graph']
    #     shortest_path_matrix = data['shortest_path_matrix']
    #     ioProcess.base_file_name = f'randomGraph{i}'
    #     renderGraph(G)
    #     print(shortest_path_matrix)
    #     print("************************************")
        

