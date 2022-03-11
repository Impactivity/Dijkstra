import sys
import heapq
import math


def dijstra(start):

    q = []
    heapq.heappush(q,(start,0))
    distance[start] = 0


    while q:
        now_node, now_dist = heapq.heappop(q)

        for next_node, next_dist in graph[now_node]:

            tot_dist = next_dist + now_dist

            if tot_dist < distance[next_node]:
                distance[next_node] = tot_dist
                heapq.heappush(q,(next_node,tot_dist))


read = sys.stdin.readline

n,m = map(int, read().split())

graph = [ []*(n+1) for _ in range(n+1)]

inf = math.inf

for _ in range(m):
    a,b,c = map(int,read().split())
    graph[a].append((b,c))  # next_node , cost
    graph[b].append((a,c)) # 쌍방향


_min = inf
distance = [inf] * (n + 1)
dijstra(1)

print(distance[n])








