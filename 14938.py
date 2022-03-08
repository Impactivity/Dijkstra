import sys
import heapq
import math

def dijkstra(start):

    queue = []
    distance = [inf] * (n+1)
    heapq.heappush(queue,[0,start]) # dist, node
    distance[start] = 0

    while queue:
        now_dst,now_node = heapq.heappop(queue)
        for next_dst,next_node in graph[now_node]: # 다음 노드 경로 탐색
            tot_dst = next_dst + now_dst
            if tot_dst < distance[next_node]:
                distance[next_node] = tot_dst
                heapq.heappush(queue, [tot_dst,next_node])
    return distance



inf = math.inf
read = sys.stdin.readline
n,m,r = map(int,read().split())
items = list(map(int,read().split()))
items.insert(0,0)


_max = 0

graph = [ [] for _ in range(n+1)]



for i in range(r):
    src,dst,dist = map(int,read().split())
    graph[src].append([dist,dst])
    graph[dst].append([dist,src])


# 탐색 시작위치
for i in range(1,n+1):
    temp_sum = 0
    # 시작노드를 1번 노드 ~ n번 노드일때 모든 경우 탐색
    result = dijkstra(i)

    for j in range(1,n+1): #distance 검색하여 m보다 작은 대상 중 item개수 최댓값 검출
        if result[j] <= m:
            temp_sum += items[j]
    _max = max(_max,temp_sum)

print(_max)

