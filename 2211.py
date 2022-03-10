import sys
import heapq
import math


read = sys.stdin.readline
# 노드, 간선의 개수 입력
n,m = map(int,read().split())
# 노드별 방문가능한 노드와 거리값 입력, 네트워크 관한 정보
graph = [ []*(n+1) for _ in range(n+1) ]

for _ in range(m):
    a,b,dist = map(int,read().split())
    graph[a].append((b,dist))
    graph[b].append((a,dist))

#변수 선언부
inf = math.inf
distance = [inf]*(n+1)
pre_nodes = [ [] for _ in range(n+1) ]



def dijkstra(start):
    q = []

    heapq.heappush(q,(start,0)) # start_node, dist
    while q:
        now_node , now_dist = heapq.heappop(q)

        for next_node, next_dist in graph[now_node]:
            tot_dist = now_dist + next_dist
            if tot_dist < distance[next_node]:
                distance[next_node] = tot_dist
                heapq.heappush(q,(next_node,tot_dist))

                # 최소 이동 비용으로 다음 노드로 이동할때 이전 노드 정보를 저장하여
                # 문제에서 요구하는 1번노드로부터 복구된(이동한) 회선들을 출력한다.
                pre_nodes[next_node] = now_node

#start 노드는 거리 비용 0
distance[1] = 0
dijkstra(1)

# 실제 이동한 회선 갯수(복구할 회선 갯수) 출력
print(len(pre_nodes[2:]))

# 1번노드에서 거친 회선들을 a b 형태로 출력 (a -> b) 노드
for i in range(len(pre_nodes)):
    if pre_nodes[i]:
        print(i, pre_nodes[i])

