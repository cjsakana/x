graph={                            # 图像graph，该点所邻接点
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D'],
    'F':['D']
    }

def BFS(grap,start):
    queue=[]                        #队列queue
    queue.append(start)
    seen=set()                      #去重，遍历过的点不再进行
    seen.add(start)
    parent={start:None}
    
    while len(queue)>0:
        vertex=queue.pop(0)         #顶点vertex
        nodes=grap[vertex]
        for w  in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w]=vertex
    return parent
parent=BFS(graph,'E')

v='B' 
while v!=None:
    print(v)
    v=parent[v]
