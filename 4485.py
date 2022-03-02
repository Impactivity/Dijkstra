import sys
import math
import heapq

read = sys.stdin.readline

inf = math.inf

dx = [0,0,-1,1]
dy = [-1,1,0,0]

count = 1

def dijkstra():

    queue = []
    heapq.heappush(queue,(graph[0][0],0,0))
    distance[0][0] = 0

    while queue:
        cost,x,y, = heapq.heappop(queue)
        if x == n-1 and y == n-1 :
            print(f'Problem {count}: {distance[x][y]}')
            break


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]

                if new_cost < distance[nx][ny] :
                    distance[nx][ny] = new_cost
                    heapq.heappush(queue,(distance[nx][ny],nx,ny))

while True:
    n = int(read())

    if n == 0:
        break

    graph = [list(map(int,read().split())) for _ in range(n)]
    distance = [ [inf] * n for _ in range(n)]

    dijkstra()
    count+=1

