import networkx as nx

from codes.algorithm import FloydGetPath
from codes.ioProcess import renderGraph, start_http_server
import tests.test_model as tm





if __name__ == '__main__':
    test_instance = tm.TestClass()
    test_instance.setup_method(test_cases_file='data/sample_test_cases/class3/lite_class3_test_cases1.json')
    sample_graph_list = test_instance.get_random_graph(10)

    G = sample_graph_list[1]
    renderGraph(G)
    start_http_server(G)
    # while True:
    #     line = input("Pleast input start and end node:")
    #     start, end = map(int, line.split())
    #     path, dist = FloydGetPath(G, start, end) 
    #     print(f"Path: {path}\nDistance: {dist}")
    #     renderGraph(G, path)


