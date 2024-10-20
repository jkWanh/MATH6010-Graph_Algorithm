import pytest
import tests.test_instance as instance
import tests.test_model as tm

@pytest.mark.group1
def test_Floyd_Pair(test_instance):
    test_instance.setup_randomtest_algorithm(instance.sampleFloydTestCasesPair)
    test_instance.random_test(10)

# def test_ParallelFloyd():
#     test_instance = tm.TestClass()
#     test_instance.setup_method(test_cases_file='data/sample_test_cases/class1/large_class1_test_cases1.json')
#     test_instance.setup_test_algorithm(sampleParallelFloydTestCases)
#     test_instance.random_test(10)

@pytest.mark.group1
def test_Dijkstra_Pair(test_instance):
    test_instance.setup_randomtest_algorithm(instance.sampleDijkstraTestCasesPair)
    test_instance.random_test(10)

@pytest.mark.group1
def test_BellmanFord_Pair(test_instance):
    test_instance.setup_randomtest_algorithm(instance.sampleBellmanFordTestCasesPair)
    test_instance.random_test(10)

@pytest.mark.group1
def test_BellmanFoldSPFA_Pair(test_instance):
    test_instance.setup_randomtest_algorithm(instance.sampleBellmanFoldSPFATestCasesPair)
    test_instance.random_test(10)

@pytest.mark.group1
def test_Floyd_Graph(test_instance):
    test_instance.setup_fulltest_algorithm(instance.sampleFloydTestCasesGraph)
    test_instance.full_graph_test()

@pytest.mark.group1
def test_Dijkstra_Graph(test_instance):
    test_instance.setup_fulltest_algorithm(instance.sampleDijkstraTestCasesGraph)
    test_instance.full_graph_test()

@pytest.mark.group1
def test_BellmanFord_Graph(test_instance):
    test_instance.setup_fulltest_algorithm(instance.sampleBellmanFordTestCasesGraph)
    test_instance.full_graph_test()

@pytest.mark.group1
def test_BellmanFoldSPFA_Graph(test_instance):
    test_instance.setup_fulltest_algorithm(instance.sampleBellmanFoldSPFATestCasesGraph)
    test_instance.full_graph_test()