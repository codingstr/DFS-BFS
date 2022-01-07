# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    
    def searchNetwork(node) :
        if computers[node][node] == 0 :
            return False
        else :
            computers[node][node] = 0
            for i in range(n) :
                if computers[node][i] == 1 :
                    searchNetwork(i)
            return True

    answer = 0
    for i in range(n) :
        if searchNetwork(i) :
            answer += 1

    return answer