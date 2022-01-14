# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words) :
    answer = 0
    queue = deque([[begin, 0]])     # 처리중인 단어, 변환한 횟수

    while queue :
        begin, distance = queue.popleft()       # 처리중인 단어, 변환한 횟수
        
        # target으로 변환되었다면 처리
        if begin == target :
            if answer == 0 or answer > distance :
                answer = distance
        # 아니라면 다음으로 탐색할 수 있는 단어를 queue에 append
        else :
            # 처리중인 단어에서 변환할 수 있는 단어들
            mutableWordsArr = words.copy()
            for word in mutableWordsArr.copy() :
                equalNum = 0
                for i, char in enumerate(word) :
                    if begin[i] == char : equalNum += 1
                if not equalNum == len(word)-1 : mutableWordsArr.remove(word)

            for word in mutableWordsArr :
                if word in words : words.remove(word)
                queue.append([word, distance+1])

    return answer

print(str(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))+", 4")