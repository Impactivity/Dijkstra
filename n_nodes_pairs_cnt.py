import heapq
import math
from itertools import permutations

inf = math.inf

# case 1
# n = 5
# edges = [[0,1],[0,2],[1,3],[1,4]]

#case 2
n = 4
edges = [[2,3],[0,1],[1,2]]


graph = [ [] * (n) for _ in range(n) ]

arr = []
nodes = [ i for i in range(n) ]


for start, end in edges:
    graph[start].append((end,1))
    graph[end].append((start,1))


def dijkstra(start, graph):

    q = []
    distance = [inf] * n

    heapq.heappush(q,(start, 0))
    distance[start] = 0

    while q :
        now_node, now_dist = heapq.heappop(q)
        if now_dist > distance[now_node]:
            continue

        for next_node ,next_dist in graph[now_node]:
            tot_dist = now_dist + next_dist

            if tot_dist < distance[next_node]:
                distance[next_node] = tot_dist
                heapq.heappush(q,(next_node,tot_dist))

    return distance[:]

for i in range(n):
    arr.append(dijkstra(i,graph))

# 3개 노드 뽑기
tmp = list(permutations(nodes,3))
cnt = 0

# 문제에서 distance(i, j) + distance(j, k) = distance(i, k)
# 만족하는 조건 대상 찾기

for i,j,k in tmp:
    if arr[i][j] + arr[j][k] == arr[i][k]:
        cnt+=1

print(cnt)


