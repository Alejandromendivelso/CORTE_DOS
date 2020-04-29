
print("Grafo de dijstra")

def dijkstra(G, a, z):
    
    assert a in G
    assert z in G

    Inf = 0
    for u in G:
        for v, w in G[u]:
            Inf += w
    L = dict([(u, Inf) for u in G]) 
    L[a] = 0
    S = set([u for u in G]) 
    A = { }

    def W(v):
        return L[v]
    while z in S:
        u = min(S, key=W)
        S.discard(u)
        for v, w in G[u]:
            if v in S:
                if L[u] + w < L[v]:
                    L[v] = L[u] + w
                    A[v] = u
    P = []
    u = z
    while u != a:
        P.append(u)
        u = A[u]
    P.append('a')
    P.reverse()
    return L[z], P
                    
G1 = { 
    'a' : [('b', 4), ('c',2)],
    'b' : [('a', 4), ('c',1), ('d',5)],
    'c' : [('a', 2), ('b',1), ('d',8), ('e',10)],
    'd' : [('b', 5), ('c',8), ('e',2), ('z', 6)],
    'e' : [('c',10), ('d',2), ('z',3)],
    'z' : [('d', 6), ('e',3)],
    }

G2 = { 
    'a' : [('b', 22), ('c',31)],
    'b' : [('a', 2), ('d',5), ('e',2)],
    'c' : [('a', 3), ('e',5)],
    'd' : [('b', 5), ('e',1), ('z',2)],
    'e' : [('b', 2), ('c',5), ('d',1), ('z',6)],
    'z' : [('d', 23), ('e',10)],
    }


if __name__ == '__main__':
    from pprint import pprint
    w, p =  dijkstra(G1, 'a', 'z')
    pprint (G1)
    pprint (p)
    pprint (w)
    w, p =  dijkstra(G2, 'a', 'z')
    pprint (G2)
    pprint (p)
    pprint (w)