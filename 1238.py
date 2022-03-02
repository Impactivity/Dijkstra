import sys
import math
import heapq

inf = math.inf

read = sys.stdin.readline

# n명의 학생이 x마을에서 모일 때 가장 오래걸리는 학생 구하기
# m개의 도로가 있다.
n,m,x = map(int,read().split())
graph = [[] for _ in range(n+1)]
result = 0

for _ in range(m):
    a,b,cost = map(int,read().split())
    graph[a].append((b,cost))


def dijstra(start):
    q = []
    distance = [inf] * (n + 1)

    heapq.heappush(q, (0,start)) #dist , start_node
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)

        # 현재 저장되어있는 거리보다 크다면 최소값 서칭할 필요가 없음
        if distance[cur] < dist:
            continue

        #cur 노드에서 갈 수 있는 노드의 inx와 cost 확인
        for node_ix, node_cost in graph[cur]:
            cost = dist + node_cost  # 현재 노드의 dist + 다음 노드 cost

            if distance[node_ix] > cost: # 다음노드까지 가는 지금까지의 distance보다 계산된 cost 작다면
                distance[node_ix] = cost #cost 저장
                heapq.heappush(q, (cost,node_ix))

    return distance


for i in range(1,n+1):
    go = dijstra(i)
    back = dijstra(x)
    result = max(result , go[x]+back[i])

print(result)