n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):

    answer = 0
    queue = []
    checked = [False] * n

    def bfs(x):
        nonlocal queue
        nonlocal checked
        nonlocal answer

        checked[x] = True
        queue.append(x)

        while len(queue) != 0:
            x = queue[0]
            del queue[0]

            for i in range(len(computers)):
                if computers[x][i] == 1 and checked[i] == False:
                    queue.append(i)
                    checked[i] = True

        answer += 1

        if False in checked:
            bfs(checked.index(False))


    bfs(0)

    return answer


answer = solution(n,computers)
print(answer)