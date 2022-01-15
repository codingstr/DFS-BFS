# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(tickets):
    answer = []
    # 도착 공항을 기준으로 ABC순 정렬
    tickets.sort(key = lambda x : x[1])
    queue = deque([['ICN', tickets, ['ICN']]])      # 현재 공항, 남은 티켓, 방문한 공항

    while queue :
        currentAirport, remainTickets, visitedAirport = queue.popleft()     # 현재 공항, 남은 티켓, 방문한 공항
        # 티켓을 모두 썼다면 break
        if remainTickets == [] :
            answer = visitedAirport
            break
        # 다음으로 방문할 수 있는 공항들을 queue에 append.
        for idx, ticket in enumerate(remainTickets) :
            if ticket[0] == currentAirport :
                queue.append([ticket[1], remainTickets[:idx]+remainTickets[idx+1:], visitedAirport+[ticket[1]]])
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print("ICN, JFK, HND, IAD")
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print("ICN, ATL, ICN, SFO, ATL, SFO")