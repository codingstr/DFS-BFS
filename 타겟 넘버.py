# https://programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # sum, length

    while queue :

        s, l = queue.popleft()
        if l > len(numbers) :
            break
        elif l == len(numbers) and s == target :
            answer += 1

        # 길이를 천천히 늘려가며 sum을 계산.
        # l==len(numbers)==n일 때 합의 경우의 수는 n^5 (l이 증가할 때마다 합의 경우의 수가 2배씩(+,-) 증가하므로)
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))
        print('합 = '+str(s))
        print('길이 = '+str(l))
        print('numbers[l-1] = '+str(numbers[l-1]))
        print('queue = '+str(queue))
        print('---------------------------------------------------------------------------')

    return answer

numbers = [1, 2, 3, 4, 5]
target = 3
print(str(solution(numbers, target))+', 3')