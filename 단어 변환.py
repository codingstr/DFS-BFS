# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words) :
    answer = 0
    queue = deque([[begin, 0]])

    def mutableWords(before) :
        mutableWordsArr = words[:] if begin == before else words[:words.index(before)]+words[words.index(before)+1:]
        for word in mutableWordsArr[:] :
            equalNum = 0
            for i in range(len(word)) :
                if before[i] == word[i] : equalNum += 1
            if not equalNum == len(word)-1 : mutableWordsArr.remove(word)
        return mutableWordsArr

    while queue :
        begin, distance = queue.popleft()
        mutableWordsArr = mutableWords(begin)
        print(begin)
        if begin == target :
            if answer == 0 or answer > distance :
                answer = distance
        else :
            for word in mutableWordsArr :
                if word in words : words.remove(word)
                queue.append([word, distance+1])
        print(list(queue))
    

    return answer

print(str(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))+", 4")