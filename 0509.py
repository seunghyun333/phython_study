#25 자료형 변환
'''
수정 불가한 튜플 수정하기
'''
#튜플 <-> 리스트 
my_tuple=('오예스', '몽쉘')
my_list = list(my_tuple)
my_list.append('초코파이')
my_tuple = tuple(my_list)

print(my_tuple)

#리스트의 중복 제거, 순서보장 x 
my_list = ['오예스', '몽쉘', '초코파이', '초코파이', '초코파이']
my_set = set(my_list)
my_list = list(my_set)
print(my_list)

#순서보장 중복 x 딕셔너리
my_list = ['오예스', '몽쉘', '초코파이', '초코파이', '초코파이']
my_dict = dict.fromkeys(my_list)
print(my_dict)
my_list = list(my_dict)
print(my_list)


#26 if 조건문1
'''
if 조건:
    이 문장 (True)
다음문장 (False)
'''

today = '화요일'
if today == '일요일':
    print('게임 한 판')
print('공부시작')


today = '화요일'
if today == '일요일':
    print('게임 한 판')
else:
    print('else')
print('공부시작')


#27 if 조건문2
'''
if, elif, elif, elif, else 
'''
today = '화요일'
if today == '일요일':
    print('게임 한 판')
elif today == '화요일':
    print('elif')
else:
    print('else')
print('공부시작')

#28 if 중첩 
yellow_card = 0
foul = False
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('조심')
else:
    print('파울아님')


#29 for 반복문

for x in range(10):
    print('뛰어')

print('---')   

for x in range(10):
    print(f'뛰기 {x}회')


#30 range
'''
range(stop)
0부터 stop 미만

range(start, stop)
start 부터 stop 미만

range(start, stop, step)
start 부터 stop 미만 step 만큼 증가
'''

for x in range(1, 10, 2):
    print(x)


#31 for 활용
my_list = [1,2,3] 
for x in my_list:
    print(x)

my_tuple = (4,5,6)
for x in my_tuple:
    print(x)

person = {'이름':'나귀욤', '나이':7, '키':120}
for x in person.values():
    print(x)

for x in person.keys():
    print(x)

for k,v in person.items():
    print(k,v)
'''
이름 나귀욤
나이 7
키 120
'''

fruit ='apple'
for aa in fruit:
    print(aa)

'''
a
p
p
l
e
'''