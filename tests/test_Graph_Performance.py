import pytest
import tests.test_model as tm
from tests.test_instance import sampleFloydTestCasesGraph, sampleDijkstraTestCasesGraph, sampleBellmanFordTestCasesGraph, sampleBellmanFoldSPFATestCasesGraph 

@pytest.mark.group3
def test_Floyd_Graph_Performance(benchmark, test_instance):
    # 设置 benchmark 的 group 属性
    benchmark.group = 'group3'  # 直接设置 group 属性

    test_instance.setup_fulltest_algorithm(sampleFloydTestCasesGraph)
    benchmark(test_instance.full_graph_test)

@pytest.mark.group3
def test_Dijkstra_Graph_Performance(benchmark, test_instance):
    # 设置 benchmark 的 group 属性
    benchmark.group = 'group3'  # 直接设置 group 属性

    test_instance.setup_fulltest_algorithm(sampleDijkstraTestCasesGraph)
    benchmark(test_instance.full_graph_test)

@pytest.mark.group3
def test_BellmanFord_Graph_Performance(benchmark, test_instance):
    benchmark.group = 'group3'

    test_instance.setup_fulltest_algorithm(sampleBellmanFordTestCasesGraph)
    benchmark(test_instance.full_graph_test)

@pytest.mark.group3
def test_BellmanFoldSPFA_Graph_Performance(benchmark, test_instance):
    benchmark.group = 'group3'

    test_instance.setup_fulltest_algorithm(sampleBellmanFoldSPFATestCasesGraph)
    benchmark(test_instance.full_graph_test)