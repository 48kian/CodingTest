'''
백트래킹
    cf) 4-queens

풀이방법
O 큐에서 ICN 부터 꺼낸다.
O 방문한 것은 checked
X ticket 두번째가 첫번째인 것을 찾는다.

'''
'''
주의사항
1. 가능한 경로가 2개 이상이면 알파벳 순서로.
'''

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "AAA"],["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

# 연결 안되어 있을 경우를 생각 못 함
def solution1(tickets):
    answer = []
    route = []
    tickets.sort()
    print(tickets)
    checked = [False] * len(tickets)
    nextAirport = "ICN"
    
    while True:
        
        for i in range(len(tickets)):
            ticket = tickets[i]
            if checked[i] == False and ticket[0] == nextAirport:
                route.append(ticket[0])
                nextAirport = ticket[1]
                checked[i] = True
        
        if len(route) == len(tickets):
            route.append(nextAirport)
            break
    
    answer = route
    print(answer)
    return answer




def solution2(tickets):
    tickets.sort()
    answer = []
    route = []

    #print(tickets)

    checked = [False] * len(tickets)
    #queue = []
    nextAirport = "ICN"
    count = 0

    def dfs(route, checked, nextAirport, count):
        nonlocal answer

        for i in range(len(tickets)):
            ticket = tickets[i]
            print(ticket)
            if checked[i] == False and nextAirport == ticket[0]:
                route.append(ticket[0])
                print("route",route)
                nextAirport = ticket[1]
                checked[i] = True
                dfs(route, checked, nextAirport, count + 1)

        route.pop()

        if len(route) == len(tickets):
            route.append(nextAirport)
            print("ddd")    

            

    dfs(route, checked, nextAirport, count)
    answer = route
    print(answer)
    return answer

solution2(tickets)
