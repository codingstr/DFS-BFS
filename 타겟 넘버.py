# https://programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # sum, length
    while queue :
        s, l = queue.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1
            print("asdf")
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))
        print('s = '+str(s))
        print('l = '+str(l))

    return answer

numbers = [1, 2, 3, 4, 5]
target = 3
print(str(solution(numbers, target))+', 3')