import pytest
import tests.test_model as tm
from tests.test_instance import sampleFloydTestCasesPair, sampleDijkstraTestCasesPair, sampleBellmanFordTestCasesPair, sampleBellmanFoldSPFATestCasesPair

@pytest.mark.group2
def test_Flyod_Pair_performance(benchmark, test_instance):
    benchmark.group = 'group2'  # 直接设置 group 属性

    # 使用 benchmark 固件来测量 sum 函数的性能
    test_instance.setup_randomtest_algorithm(sampleFloydTestCasesPair)
    benchmark(test_instance.random_test, 10)

# def test_ParallelFlyod_performance(benchmark):
#     # 使用 benchmark 固件来测量 sum 函数的性能
#     test_instance = tm.TestClass()
#     test_instance.setup_method(test_cases_file='data/sample_test_cases/class1/large_class1_test_cases1.json')
#     test_instance.setup_test_algorithm(sampleParallelFloydTestCases)
#     benchmark(test_instance.random_test, 10)

@pytest.mark.group2
def test_Dijsktra_Pair_performance(benchmark, test_instance):
    # 设置 benchmark 的 group 属性
    benchmark.group = 'group2'  # 直接设置 group 属性

    test_instance.setup_randomtest_algorithm(sampleDijkstraTestCasesPair)
    benchmark(test_instance.random_test, 10)

@pytest.mark.group2
def test_BellmanFord_Pair_performance(benchmark, test_instance):
    benchmark.group = 'group2'

    test_instance.setup_randomtest_algorithm(sampleBellmanFordTestCasesPair)
    benchmark(test_instance.random_test, 10)

@pytest.mark.group2
def test_BellmanFoldSPFA_Pair_performance(benchmark, test_instance):
    # 设置 benchmark 的 group 属性
    benchmark.group = 'group2'  # 直接设置 group 属性

    test_instance.setup_randomtest_algorithm(sampleBellmanFoldSPFATestCasesPair)
    benchmark(test_instance.random_test, 10)