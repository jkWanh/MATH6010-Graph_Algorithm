import networkx as nx
import graphviz
import os
import random
from FloydWarshall import Floyd

# 设置输出目录与检查
dot_output_directory = 'graphs/'  
png_output_directory = 'photos/'
os.makedirs(dot_output_directory, exist_ok=True)
os.makedirs(png_output_directory, exist_ok=True)
base_file_name = 'randomGraph1'

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
# dot.render(f'{dot_output_directory}{base_file_name}', format='dot')  # 生成 dot 文件
dot.render(f'{png_output_directory}{base_file_name}', format='png', view=True)  # 生成 PNG 文件
os.rename(f'{png_output_directory}{base_file_name}', f'{dot_output_directory}{base_file_name}')  # 删除 dot 文件