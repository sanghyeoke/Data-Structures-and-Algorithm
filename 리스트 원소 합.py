'''
문제 설명
입력으로 주어지는 리스트 x 의 첫 원소와 마지막 원소의 합을 리턴하는 함수 solution() 을 완성하세요.
'''

x = [1, 4, 5, 7]
def solution(x):
    answer = x[0] + x[-1]
    return answer

print(solution(x))