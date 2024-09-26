from graphviz import Digraph

dot = Digraph()

# 添加节点和边
dot.node('A')
dot.node('B')
dot.node('C')
dot.node('D')

dot.edges(['AB', 'AC', 'BD'])

# 渲染图
dot.render('graph', format='png', view=True)
