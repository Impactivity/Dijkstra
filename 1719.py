import sys
import math
import heapq

read = sys.stdin.readline
inf = math.inf
n,m = map(int,read().split())

graph = [[]*(n+1) for _ in range(m+1)]
dist_map = [ [0]*(n+1) for _ in range(n+1) ]


for _ in range(m):
    src,dst,dist = map(int,read().split())
    graph[src].append([dst,dist])
    graph[dst].append([src,dist])

def dijkstra(start):
    heapq.heappush(q,( start , 0) ) # start, dist
    distance[start] = 0

    while q:
        now_node,now_dist = heapq.heappop(q)
        for next_node, next_dist in graph[now_node]:
            tot_dist = next_dist + now_dist
            if tot_dist < distance[next_node]:
                distance[next_node] = tot_dist
                heapq.heappush(q, (next_node, tot_dist))
                # now_node가 제일먼저 거쳐야할 노드
                dist_map[next_node][start] = now_node

for i in range(1,n+1):
    q = []
    distance = [inf] * (n+1)

    dijkstra(i)

# 행 번째 노드에서 -> 열 번째 노드로 이동할 때 가장 먼저 거쳐야할 노드 표시
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j :
            print('-', end=' ')
        else:
            print(dist_map[i][j], end=' ')
    print()