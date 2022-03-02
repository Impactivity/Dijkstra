import sys
import math

inf = math.inf

read = sys.stdin.readline

# n명의 학생이 x마을에서 모일 때 가장 오래걸리는 학생 구하기
# m개의 도로가 있다.
n,m,x = map(int,read().split())
# src, dst , cost
roads = [list(map(int, read().split())) for _ in range(m)]

costs = [[inf] * (n+1) for _ in range(n+1)]


for i in roads:
    costs[i[0]][i[0]] = 0
    costs[i[0]][i[1]] = i[2]


def dijstra(start,dst):
    distance = [inf] * (n + 1)

    for i in range(1,n+1):
        if distance[start][dst] > costs[start][i] + costs[i][dst]:
            distance[start][dst] = costs[start][i] + costs[i][dst]






print(costs)

