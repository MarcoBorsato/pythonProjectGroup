from graph import *
from graph_io import *


def color_ref(g: Graph) -> Graph:
    colors = {}
    stored = 0
    for v in g.vertices:
        v.colornum = v.degree
        if v.degree in colors:
            colorList = []
            for w in v.neighbours:
                colorList.append([w, w.degree])
            sorted(colorList, key=lambda x: x[1])
            colors[v.colornum].append(colorList)
        else:
            colorList = []
            for w in v.neighbours:
                colorList.append([w, w.degree])
            sorted(colorList, key=lambda x: x[1])
            colors[v.colornum] = colorList

    print(colors)
    i = max(colors)

    j = colors[min(colors)]
    compare = j[0]
    print(j)
    # for k in colors[j]:
    #     if k != compare:



if __name__ == '__main__':
    with open('cref9vert_4_9.grl') as f:
        L = load_graph(f, read_list=True)

    color_ref(L[0][0])
    # with open('colorful.dot', 'w') as f:
    #     write_dot(H, f)
