# MATH6010-Graph_Algorithm

MATH6010 class projects

## 测试模块

设置7类测试集合：(仅考虑简单图，不含重边和自环)

1. 非负边权重图（含有向图&无向图，边权重$[0,100]$）
2. 含负边权重图（含负权重边的有向图，边权重$[-50,50]$，无负权重环）
3. 非负边权重稀疏图（含有向图&无向图，边权重$[0,100]$，$|E| < 3\cdot|V|$）
4. 非负边权重稠密图（含有向图&无向图，边权重$[0,100]$，$|E| > 0.5\cdot|V|^2$）
5. 含负边权重稀疏图（含负权重边有向图，边权重$[-50,50]$，$|E| < 3\cdot|V|$，无负权重环）
6. 含负边权重稠密图（含负权重边有向图，边权重$[-50,50]$，$|E| > 0.5\cdot|V|^2$，无负权重环）  
7. 负权重环图（含有向图&无向图，边权重$[-50,50]$且至少有向图有一个负权重环, 无向图至少含有一条负权重边）
8. 混合模式（混合34567）

- 测试类接口：

1. [x] 加载现有测试集合
2. [x] 最短路随机测试
3. [ ] 最短路全量测试
4. [ ] 手工测试-随机生成图
