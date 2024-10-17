import networkx as nx
import graphviz
import http.server
import socketserver
import os
import fcntl
import webbrowser
import threading
import random
import re

from flask import Flask, request, render_template_string, send_from_directory
from typing import Union
from codes.algorithm import FloydGetPath

app = Flask(__name__)
file_lock = threading.Lock()
Graph = nx.Graph()

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

# HTML模板
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Graph Viewer</title>
</head>
<body>
    <h1>Graph Viewer</h1>
    <form method="post">
        <label for="input">Input:</label>
        <input type="text" id="input" name="input">
        <button type="submit">Submit</button>
    </form>
    <h2>Output:</h2>
    <p>{{ output }}</p>
    <img src="{{ url_for('serve_image', filename=image_url) }}" alt="Graph Image">
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    image_url = "randomGraph1.png"  # 默认图像文件
    if request.method == 'POST':
        user_input = request.form['input']
        # 处理用户输入并生成输出
        output = f"Processed input: {user_input}"
        # 这里可以添加处理用户输入的逻辑，例如更新图像文件等
        if re.match(r'^\d+\s+\d+$', user_input):
            start, end = map(int, user_input.split())
            path, dist = FloydGetPath(Graph, start, end)
            renderGraph(Graph, path)
            output = f"Path: {path}\nDistance: {dist}"
        else:
            output = "Invalid input format. Please enter two integers separated by a space."
    return render_template_string(html_template, output=output, image_url=image_url)

@app.route('/data/photos/<path:filename>')
def serve_image(filename):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    image_dir = os.path.join(base_dir, 'data/photos')
    print(image_dir)
    return send_from_directory(image_dir, filename)

def change_edge_color(dot, start, end, label, color):
    # 创建一个新的 Graphviz 对象
    new_dot = graphviz.Digraph() if isinstance(dot, graphviz.Digraph) else graphviz.Graph()
    
    # 遍历原始 dot 对象的边，修改指定边的颜色
    for line in dot.source.split('\n'):
        if f'{start} -> {end} [label="{label}"]' in line:
            new_dot.edge(start, end, label=label, color=color)
        else:
            new_dot.source += line + '\n'
    
    return new_dot

def renderGraph(G: Union[nx.Graph, nx.DiGraph], path: list = None):
    # 创建一个 Graphviz 的 graph 对象
    if isinstance(G, nx.DiGraph):
        dot = graphviz.Digraph()
    else:
        dot = graphviz.Graph()

    # 添加节点和边
    for node in G.nodes():
        dot.node(str(node), shape='circle', label=str(node), style='filled', fillcolor='lightblue')

    if path:
        if isinstance(G, nx.DiGraph):
            for edge in G.edges():
                if (edge[0], edge[1], G[edge[0]][edge[1]]['weight']) in path:
                    dot.edge(str(edge[0]), str(edge[1]), label=str(G[edge[0]][edge[1]]['weight']), color='red')
                else:
                    dot.edge(str(edge[0]), str(edge[1]), label=str(G[edge[0]][edge[1]]['weight']))
        else:
            for edge in G.edges():
                if (edge[0], edge[1], G[edge[0]][edge[1]]['weight']) in path or (edge[1], edge[0], G[edge[1]][edge[0]]['weight']) in path:
                    dot.edge(str(edge[0]), str(edge[1]), label=str(G[edge[0]][edge[1]]['weight']), color='red')
                else:
                    dot.edge(str(edge[0]), str(edge[1]), label=str(G[edge[0]][edge[1]]['weight']))
    else:
        for edge in G.edges():
            dot.edge(str(edge[0]), str(edge[1]), label=str(G[edge[0]][edge[1]]['weight']))

    # 渲染图
    with file_lock:
        dot.render(f'{png_output_directory}{base_file_name}', format='png', view=False)  # 生成 PNG 文件
    os.rename(f'{png_output_directory}{base_file_name}', f'{dot_output_directory}{base_file_name}')  # 移动 dot 文件

def start_http_server(graph):
    global Graph
    Graph = graph
    PORT = 8000
    with file_lock:
        webbrowser.open(f'http://localhost:{PORT}/')
    renderGraph(Graph)
    app.run(port=PORT)

