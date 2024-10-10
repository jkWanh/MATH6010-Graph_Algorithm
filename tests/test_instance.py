import pytest

import networkx as nx
import numpy as np

import tests.test_cases as tc
import tests.test_model as tm

from codes.algorithm import Floyd, Floyd2
i = 0
def sampleFloydTestCases(graph: nx.Graph, start: int, end: int) -> float:
    global i
    if i < 10:
        ans_matrix = Floyd(graph)
        # i += 1
        return ans_matrix[start][end]
    else:
        return np.nan
    

def test_Floyd():
    test_instance = tm.TestClass()
    test_instance.setup_method(test_cases_file='data/sample_test_cases/class1/large_class1_test_cases1.json')

    with pytest.raises(ValueError, match="missing test_algorithm parameter"):
        test_instance.random_test()

    with pytest.raises(ValueError, match="test_algorithm should accept 3 parameters"):
        test_instance.random_test(lambda x: x)

    with pytest.raises(ValueError, match="test_algorithm should return float type"):
        def wrong_return_type_algorithm(G: nx.Graph, start: int, end: int) -> int:
            return 42
        test_instance.random_test(wrong_return_type_algorithm)

    test_instance.random_test(sampleFloydTestCases, 10)

def test_performance(benchmark):
    # 使用 benchmark 固件来测量 sum 函数的性能
    test_instance = tm.TestClass()
    test_instance.setup_method(test_cases_file='data/sample_test_cases/class1/large_class1_test_cases1.json')
    benchmark(test_instance.random_test, sampleFloydTestCases, 10)


if __name__ == '__main__':
    pytest.main(['-s', 'test_instance.py'])
