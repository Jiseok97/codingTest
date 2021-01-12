# 큰 수의 법칙
# 배열의 크기: N, 숫자가 더해지는 횟수: M, 최댓값 더할 수 있는 횟수: K
# 입력 : N M K
# 입력 예시: 5 8 3
#           2 4 5 4 6
# 출력 예시: 46

# 모범 코드

# # N, M, K 를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))

# data.sort() # 입력 받은 수들 정렬하기
# first = data[n - 1] # 가장 큰 수
# second = data[n - 2] # 두 번째로 큰 수

# result = 0

# while True:
#   for i in range(k): # 가장 큰 수를 K번 더하기
#     if m == 0:  # m이 0이라면 반복문 탈출
#       break
#     result += first
#     m -= 1 # 더할 때마다 1씩 빼기
#   if m == 0: # m이 0이라면 반복문 탈출
#     break
#   result += second # 두 번쨰로 큰 수를 한번 더하기
#   m -= 1 # 더할 때마다 1씩 빼기

# print(result)




# 내가 푼 코드

input_data = list(map(int, input().split()))
number_data = list(map(int, input().split()))

number_data.sort(reverse=True)
print(number_data)
result = 0
count = 0
for i in range(input_data[1]):
  if count == input_data[2]:
    count = 0
    result += number_data[1]
  else:
    result += number_data[0]
    count += 1

print(result)
