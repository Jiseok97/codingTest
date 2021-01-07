# page: 322
# 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력되어 주어짐
# 알파벳은 오름차순으로, 모든 숫자는 더해서 이어서 출력

# 입력 예시: K1KA5CB7
# 출력 예시: ABCKK13

# 모범 코드

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
  # 알파벳인 경우 결과 리스트에 삽입
  if x.isalpha():
    result.append(x)
  # 숫자는 따로 더하기
  else:
    value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))




# 내가 푼 코드 (못 품)

# input_data = list(input())
# data=[]

# print(input_data)
# total = 0
# for test in input_data:
#   if int(test) <= int(ord('A')):
#     total += int(test)
#     input_data.remove(test)
#   else:
#     data += test

# data.append(total)
# print(data)