import heapq

N = int(input())
for i in range(N):
    min_queue,max_queue = [],[]
    visited = [False] *  1000001
    T= int(input())
    for j in range(T):
        c = input().split()
        if c[0]  ==  'I':
            heapq.heappush(min_queue,(int(c[1]),j))
            heapq.heappush(max_queue,(int(c[1])*-1,j))
            visited[j]= True
        elif c[0] == 'D':
            if c[1] == '-1':
                while min_queue and not visited[min_queue[0][1]]:
                    heapq.heappop(min_queue)
                if min_queue:
                    visited[min_queue[0][1]] = False
                    heapq.heappop(min_queue)
            if c[1] == '1':
                while max_queue and not visited[max_queue[0][1]]:
                    heapq.heappop(max_queue)
                if max_queue:
                    visited[max_queue[0][1]] = False
                    heapq.heappop(max_queue)

    while min_queue and not visited[min_queue[0][1]]:
        heapq.heappop(min_queue)
    while max_queue and not visited[max_queue[0][1]]:
        heapq.heappop(max_queue)

    if min_queue and max_queue:
        print(-max_queue[0][0], min_queue[0][0])
    else:
        print('EMPTY')


