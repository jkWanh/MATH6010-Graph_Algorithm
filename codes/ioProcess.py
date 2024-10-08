import networkx as nx
import graphviz
import os
import random

from typing import Union

# 设置输出目录与检查
dot_output_directory = 'data/graphs/'  
png_output_directory = 'data/photos/'
try:
    os.makedirs(dot_output_directory, exist_ok=True)
    os.makedirs(png_output_directory, exist_ok=True)
except:
    print('Directory already exists')
    exit(1)
base_file_name = 'randomGraph1'

def renderGraph(G: Union[nx.Graph, nx.DiGraph]):
    # 创建一个 Graphviz 的 graph 对象
    if isinstance(G, nx.DiGraph):
        dot = graphviz.Digraph()
    else:
        dot = graphviz.Graph()

    # 添加节点和边
    for node in G.nodes():
        dot.node(str(node), shape='circle', label=str(node), style='filled', fillcolor='lightblue')

    for edge in G.edges():
        dot.edge(str(edge[0]), str(edge[1]), label=str(G[edge[0]][edge[1]]['weight']))

    # 渲染图
    dot.render(f'{png_output_directory}{base_file_name}', format='png', view=False)  # 生成 PNG 文件
    os.rename(f'{png_output_directory}{base_file_name}', f'{dot_output_directory}{base_file_name}')  # 移动 dot 文件