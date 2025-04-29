print('hello world')
print("안녕하세요")
print(True)
print(False)
print(10)

# 변수
age = 7
print(age)

# 변수 이름
# 1. 문자 또는 _로 시작, 숫자로 시작할 수 없음 ! 
# 2. 문자, 숫자, _로 구성
# 3. 공백 x, 특수문자 x 
# 4. 대소문자 구분 
# 5. 키워드(예약어)x, True, False, for, while, if, continue, break, class 
# 6. 소문자 단어, _로 구분도니 단어들(권장)



#6. 형변환 
#int()정수로, float()실수로, str() 문자로
#괄호 속은 반드시 알아볼 수 있는 형태로 

num = int(float('2.5')) #소수점 이하는 버림됨 
print(num) 

#7. 연산자
# +,-,*,/,% 나머지, // 몫, ** 거듭제곱 , == 같다, != 같지 않다 
# and : 둘다 참, or 하나라도 참이면 참, not 반전
# 멤버연산자 : in 포함 , not in 미포함 
print('c' in 'cat')
print('c' not in 'cat')
