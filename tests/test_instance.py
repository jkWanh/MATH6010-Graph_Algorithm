import pytest

import networkx as nx
import numpy as np

import tests.test_cases as tc
import tests.test_model as tm

from codes.algorithm import Floyd, Dijkstra, BellmanFord, BellmanFoldSPFA, ParallelFloyd

def sampleFloydTestCasesPair(graph: nx.Graph, start: int, end: int) -> float:
    ans_matrix = Floyd(graph)
    return ans_matrix[start][end]

def sampleParallelFloydTestCasesPair(graph: nx.Graph, start: int, end: int) -> float:
    ans_matrix = ParallelFloyd(graph)
    return ans_matrix[start][end]

def sampleDijkstraTestCasesPair(graph: nx.Graph, start: int, end: int) -> float:
    anslist = Dijkstra(graph, start)
    return anslist[end]

def sampleBellmanFordTestCasesPair(graph: nx.Graph, start: int, end: int) -> float:
    anslist = BellmanFord(graph, start)
    return anslist[end]
    
def sampleBellmanFoldSPFATestCasesPair(graph: nx.Graph, start: int, end: int) -> float:
    anslist = BellmanFoldSPFA(graph, start)
    return anslist[end]

def sampleFloydTestCasesGraph(graph: nx.Graph) -> np.ndarray:
    return Floyd(graph)

def sampleParallelFloydTestCasesGraph(graph: nx.Graph) -> np.ndarray:
    return ParallelFloyd(graph)

def sampleDijkstraTestCasesGraph(graph: nx.Graph) -> np.ndarray:
    n = len(graph)
    dist = np.full((n, n), np.inf)
    for i in range(n):
        dist[i] = Dijkstra(graph, i)
    return dist

def sampleBellmanFordTestCasesGraph(graph: nx.Graph) -> np.ndarray:
    n = len(graph)
    dist = np.full((n, n), np.inf)
    for i in range(n):
        dist[i] = BellmanFord(graph, i)
    return dist

def sampleBellmanFoldSPFATestCasesGraph(graph: nx.Graph) -> np.ndarray:
    n = len(graph)
    dist = np.full((n, n), np.inf)
    for i in range(n):
        dist[i] = BellmanFoldSPFA(graph, i)
    return dist



# def test_Flyod_performance(benchmark):
#     # 使用 benchmark 固件来测量 sum 函数的性能
#     test_instance = tm.TestClass()
#     test_instance.setup_method(test_cases_file='data/sample_test_cases/class1/large_class1_test_cases1.json')
#     test_instance.setup_test_algorithm(sampleFloydTestCases)
#     benchmark(test_instance.random_test, 10)


# def test_ParallelFlyod_performance(benchmark):
#     # 使用 benchmark 固件来测量 sum 函数的性能
#     test_instance = tm.TestClass()
#     test_instance.setup_method(test_cases_file='data/sample_test_cases/class1/large_class1_test_cases1.json')
#     test_instance.setup_test_algorithm(sampleParallelFloydTestCases)
#     benchmark(test_instance.random_test, 10)

# def test_Dijsktra_performance(benchmark):
#     test_instance = tm.TestClass()
#     test_instance.setup_method(test_cases_file='data/sample_test_cases/class1/large_class1_test_cases1.json')
#     test_instance.setup_test_algorithm(sampleDijkstraTestCases)
#     benchmark(test_instance.random_test, 10)

# def test_BellmanFord_performance(benchmark):
#     test_instance = tm.TestClass()
#     test_instance.setup_method(test_cases_file='data/sample_test_cases/class1/large_class1_test_cases1.json')
#     test_instance.setup_test_algorithm(sampleBellmanFordTestCases)
#     benchmark(test_instance.random_test, 10)

# if __name__ == '__main__':
#     pytest.main(['-s', 'test_instance.py'])
