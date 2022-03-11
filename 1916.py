import sys
import heapq
import math


read = sys.stdin.readline

n = int(read()) # n개의 노드
m = int(read()) # m개의 간선

graph = [ []*(n+1) for _ in range(n+1) ]

for i in range(m):
    src,dst,dist = map(int,read().split())
    graph[src].append((dst,dist)) # 단방향임을 주의하자.


#현재 노드, 최종 노드 입력받기
start_node, end_node = map(int,read().split())

def dijkstra(start):

    q = []
    heapq.heappush(q,(start,0))
    distance[start] = 0

    while q:
        now_node, now_dist = heapq.heappop(q)

        # 현재 노드까지 오는 최소 비용이 현재 계산된 거리값보다 최소라면 더이상 계산할 필요가 없다.
        if now_dist > distance[now_node]:
            continue
        # 다음노드 까지 가는 최소비용 계산
        for next_node, next_dist in graph[now_node]:
            tot_dist = now_dist + next_dist
            if tot_dist < distance[next_node]:
                distance[next_node] = tot_dist
                heapq.heappush(q,(next_node, tot_dist))



inf = math.inf

distance = [inf]*(n+1)

dijkstra(start_node)
print(distance[end_node])


