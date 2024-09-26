import networkx as nx
import graphviz
import random
from FloydWarshall import Floyd

# 生成一个随机图
G = nx.erdos_renyi_graph(n=10, p=0.3)
for (u,v) in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)

# 创建一个 Graphviz 的 graph 对象
dot = graphviz.Graph()

# 添加节点和边
for node in G.nodes():
    dot.node(str(node))

for edge in G.edges():
    dot.edge(str(edge[0]), str(edge[1]), label=str(G[edge[0]][edge[1]]['weight']))

dist = Floyd(G)

for line in dist:
    print(line)
    

# 渲染图
dot.render('random_graph', format='png', view=True)