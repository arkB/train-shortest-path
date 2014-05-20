#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pylab as plt

if __name__ == '__main__':
    graph = nx.DiGraph()
    # ノードを追加する
    graph.add_node('s')
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('t')
    # ノード間をエッジでつなぐ
    graph.add_edge('s', 'a', weight=2)
    graph.add_edge('s', 'b', weight=5)
    graph.add_edge('a', 'b', weight=2)
    graph.add_edge('a', 'c', weight=5)
    graph.add_edge('b', 'c', weight=4)
    graph.add_edge('b', 'd', weight=2)
    graph.add_edge('c', 't', weight=7)
    graph.add_edge('d', 'c', weight=5)
    graph.add_edge('d', 't', weight=2)
    # ダイクストラ法で最短経路を探す
    print nx.dijkstra_path(graph, 's', 't')
    print nx.dijkstra_path_length(graph, 's', 't')
    nx.draw(graph)
    plt.show()
