import networkx as nx
import time
import random
from codes.algorithm import FloydGetPath, ParallelFloyd, Floyd, BellmanFoldSPFA, BellmanFord
from codes.ioProcess import renderGraph, start_http_server
import tests.test_model as tm
from tests.test_instance import sampleParallelFloydTestCases, sampleFloydTestCases
import asyncio
import matplotlib.pyplot as plt


# async def main(nodes):
#     # test_instance = tm.TestClass()
#     # test_instance.setup_method(test_cases_file='data/sample_test_cases/class1/large_class1_test_cases1.json')
#     # sample_graph_list = test_instance.get_random_graph(1)

#     # G = sample_graph_list[0]
#     # renderGraph(G)
#     # start_http_server(sample_graph_list)
#     # while True:
#     #     line = input("Pleast input start and end node:")
#     #     start, end = map(int, line.split())
#     #     path, dist = FloydGetPath(G, start, end) 
#     #     print(f"Path: {path}\nDistance: {dist}")
#     #     renderGraph(G, path)
#     # renderGraph(G)
#     # nodes = 300
#     G = nx.erdos_renyi_graph(nodes, 0.3, directed=True)
#     for (u,v) in G.edges():
#         G[u][v]['weight'] = random.randint(1, 10)
    
#     start = time.time()
#     dict1 = Floyd(G)
#     end = time.time()
#     # print(dict)
#     t1 = end - start
#     print(f"Time: {end - start}")
#     print("******************************Parallel Floyd******************************")
#     start = time.time()
#     dict2 = await ParallelFloyd(G)
#     end = time.time()
#     # print(dict2)
#     print(f"Time: {end - start}")
#     t2 = end - start
#     for i in range(nodes):
#         for j in range(nodes):
#             if dict1[i][j] != dict2[i][j]:
#                 print(f"Error: {i} {j}, {dict1[i][j]} {dict2[i][j]}")
#                 break
#     return (t1,t2)
#     # start = time.time()
#     # test_instance.setup_test_algorithm(sampleParallelFloydTestCases)
#     # test_instance.random_test(1)
#     # end = time.time()
#     # print(f"Time: {end - start}")
#     # print("******************************Floyd******************************")
#     # start = time.time()
#     # test_instance.setup_test_algorithm(sampleFloydTestCases)
#     # test_instance.random_test(1)
#     # end = time.time()
#     # print(f"Time: {end - start}")

#     # start = time.time()
#     # sampleParallelFloydTestCases(sample_graph_list[0], 0, 1)
#     # end = time.time()
#     # print(f"Time: {end - start}")
#     # start = time.time()
#     # sampleFloydTestCases(sample_graph_list[0], 0, 1)
#     # end = time.time()
#     # print(f"Time: {end - start}")


 

if __name__ == '__main__':
    # t1l, t2l = [], []
    # for i in range(100, 300):
    #     t1, t2 = asyncio.run(main(i))
    #     t1l.append(t1)
    #     t2l.append(t2)
    # plt.plot(range(100, 300), t1l, label='Floyd')
    # plt.plot(range(100, 300), t2l, label='Parallel Floyd')
    # plt.legend()
    # plt.show()


    test_instance = tm.TestClass()
    test_instance.setup_method(test_cases_file='data/sample_test_cases/class3/medium_class3_test_cases1.json')
    sample_graph_list = test_instance.get_random_graph(1)

    G = sample_graph_list[0]
    # G = nx.erdos_renyi_graph(10, 0.3, directed=False)
    # for (u,v) in G.edges():
    #     G[u][v]['weight'] = random.randint(1, 10)
    # renderGraph(G)
    # start_http_server(sample_graph_list)
    # while True:
    #     line = input("Pleast input start and end node:")
    #     start, end = map(int, line.split())
    #     path, dist = FloydGetPath(G, start, end) 
    #     print(f"Path: {path}\nDistance: {dist}")
    #     renderGraph(G, path)
    renderGraph(G)
    dict1 = BellmanFord(G, 0)
    #print(dict)
    print("******************************Parallel Floyd******************************")
    dict2 = BellmanFoldSPFA(G, 0)
    #print(dict)
    flag = False
    for i in range(len(dict1)):
        if dict1[i] != dict2[i]:
            print(f"Error: {i}, {dict1[i]} {dict2[i]}")
            flag = True
            break
    if flag:
        print(dict1)
        print(dict2)
    else:
        print("Correct")
            
    

    # start = time.time()
    # test_instance.setup_test_algorithm(sampleParallelFloydTestCases)
    # test_instance.random_test(1)
    # end = time.time()
    # print(f"Time: {end - start}")
    # print("******************************Floyd******************************")
    # start = time.time()
    # test_instance.setup_test_algorithm(sampleFloydTestCases)
    # test_instance.random_test(1)
    # end = time.time()
    # print(f"Time: {end - start}")

    # start = time.time()
    # sampleParallelFloydTestCases(sample_graph_list[0], 0, 1)
    # end = time.time()
    # print(f"Time: {end - start}")
    # start = time.time()
    # sampleFloydTestCases(sample_graph_list[0], 0, 1)
    # end = time.time()
    # print(f"Time: {end - start}")


